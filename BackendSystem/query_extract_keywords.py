import requests
import nltk
import pyrebase

# connect to Firebase
config = {
    'apiKey': 'AIzaSyD-Fy3mSos_QBShFXgrqGNp_Vh78UUR-ew',
    'authDomain': 'easyfly-3cc98.firebaseapp.com',
    'databaseURL': 'https://easyfly-3cc98.firebaseio.com',
    'storageBucket': 'easyfly-3cc98.appspot.com',
    'messagingSenderId': '135959500080',
    'serviceAccount': 'easyfly-3cc98-68315a10130a.json'
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

text_to_interpret = db.child("textToInterpret").get().val()

while True:
    # keep script on forever until manually stopped
    if text_to_interpret != db.child('textToInterpret').get().val():
        text_to_interpret = db.child("textToInterpret").get().val()

        # connect to Microsoft Azure Cognitive Services API and initialize data
        subscription_key = '580b4851c7bd4b77824548dd5bd6c593'
        text_analytics_base_url = 'https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/'
        key_phrase_api_url = text_analytics_base_url + 'keyPhrases'
        documents = {'documents': [{'id': '1', 'language': 'en', 'text': text_to_interpret}]}
        headers = {'Ocp-Apim-Subscription-Key': subscription_key}
        response = requests.post(key_phrase_api_url, headers=headers, json=documents)

        # find the keywords from the data and return it in a uniform format
        important_words_msft_API = [i['keyPhrases'] for i in response.json()['documents']]
        key_phrases_POS_tagged = [nltk.pos_tag(nltk.word_tokenize(i['text'])) for i in documents['documents']][0]

        important_words_POS_tags = []
        for i in documents['documents']:
            tokenized_sentence = nltk.word_tokenize(i['text'])
            keywords_POS_tags = [j for j in tokenized_sentence if (j[0].isupper() and j != tokenized_sentence[0]) or
                                 any(k.isdigit() for k in j)]
            tokenized_sentence_POS_tagged = nltk.pos_tag(tokenized_sentence)
            for j in tokenized_sentence_POS_tagged:
                if j[1] == 'NNP' or j[1] == 'NNPS' or j[1] == 'CD':
                    if j[0] in keywords_POS_tags:
                        keywords_POS_tags[keywords_POS_tags.index(j[0])] = j
            important_words_POS_tags.append(keywords_POS_tags)
        important_words_POS_tags = important_words_POS_tags[0]

        important_words_msft_API = important_words_msft_API[0]
        if 'flight' in important_words_msft_API:
            del important_words_msft_API[important_words_msft_API.index('flight')]
        elif 'flights' in important_words_msft_API:
            del important_words_msft_API[important_words_msft_API.index('flights')]

        final_output = ['', '', '', '', '', '', '', '']

        # start location
        for i in key_phrases_POS_tagged:
            if i[1] in ('NNP', 'NNPS') and i[0] not in ('January', 'February', 'March', 'April', 'May', 'June', 'July',
                                                        'August', 'September', 'October', 'November', 'December') \
                    and i[0] not in list(range(100)) and i[0] in important_words_msft_API:
                final_output[0] = i[0]
                break

        # end location
        for i in key_phrases_POS_tagged:
            if i[1] in ('NNP', 'NNPS') and i[0] not in ('January', 'February', 'March', 'April', 'May', 'June',
                                                        'July', 'August', 'September', 'October', 'November',
                                                        'December') and i[0] not in list(range(100)) \
                    and i[0] in important_words_msft_API:
                final_output[1] = i[0]

        # start month
        for i in key_phrases_POS_tagged:
            if i[1] == 'NNP' and i[0] in ('January', 'February', 'March', 'April', 'May', 'June', 'July',
                                          'August', 'September', 'October', 'November', 'December'):
                final_output[2] = i[0]

        # start day
        for idx, val in enumerate(key_phrases_POS_tagged):
            if val[1] == 'CD' or val[0] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9') \
                    and key_phrases_POS_tagged[idx - 1] in ('January', 'February', 'March', 'April', 'May', 'June',
                                                            'July', 'August', 'September', 'October', 'November',
                                                            'December'):
                final_output[3] = val[0]

        # number of tickets
        for idx, val in enumerate(key_phrases_POS_tagged):
            if (val[1] == 'CD' or val[0] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')) \
                    and any(i[0] == 'tickets' for i in key_phrases_POS_tagged):
                final_output[6] = val[0]

        # boarding class
        for i in key_phrases_POS_tagged:
            if i[1] in ('NN', 'JJ') and i[0] in ('economy', 'business', 'first'):
                final_output[7] = i[0]

        print(f'\nFINAL OUTPUT: {final_output}')
        print(f'TEXT TO INTERPRET: {text_to_interpret}\n')

        # start location
        db.child('from').set(final_output[0])
        print(f'from: {final_output[0]}')

        # end location
        db.child('to').set(final_output[1])
        print(f'to: {final_output[1]}')

        # start month
        db.child('departMonth').set(final_output[2])
        print(f'departMonth: {final_output[2]}')

        # start day
        db.child('departDay').set(final_output[3])
        print(f'departDay: {final_output[3]}')

        # end month
        db.child('returnMonth').set(final_output[4])
        print(f'returnMonth: {final_output[4]}')

        # end day
        db.child('returnDay').set(final_output[5])
        print(f'returnDay: {final_output[5]}')

        # num people
        db.child('numOfPassengers').set(final_output[6])
        print(f'numOfPassengers: {final_output[6]}')

        # boarding class
        db.child('class').set(final_output[7])
        print(f'class: {final_output[7]}')
