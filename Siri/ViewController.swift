
import UIKit
import Speech

class ViewController: UIViewController, SFSpeechRecognizerDelegate {
	
	@IBOutlet weak var textView: UITextView!
	@IBOutlet weak var microphoneButton: UIButton!
    private let speechRecognizer = SFSpeechRecognizer(locale: Locale.init(identifier: "en-US"))!
    private var recognitionRequest: SFSpeechAudioBufferRecognitionRequest?
    private var recognitionTask: SFSpeechRecognitionTask?
    private let audioEngine = AVAudioEngine()

    
    // add more code
    private var finalInformationList = ["","","","","","","",""];
    public var tempInformationList = ["","","","","","","",""];
    @IBOutlet weak var startingLocationTextField: UITextField!
    @IBOutlet weak var endingLocationTextField: UITextField!
    @IBOutlet weak var departMonthTextField: UITextField!
    @IBOutlet weak var departDayTextField: UITextField!
    @IBOutlet weak var returnMonthTextField: UITextField!
    @IBOutlet weak var returnDayTextField: UITextField!
    @IBOutlet weak var numOfPassengersTextField: UITextField!
    @IBOutlet weak var classTextField: UITextField!
    @IBOutlet weak var nextPageButton: UIButton!
    
    
	override func viewDidLoad() {
        super.viewDidLoad()
        microphoneButton.setImage(UIImage(named: "mic"), for: .normal)
        let tap = UITapGestureRecognizer(target: self.view, action: #selector(UIView.endEditing(_:)))
        tap.cancelsTouchesInView = false
        self.view.addGestureRecognizer(tap)
        
        microphoneButton.isEnabled = false
        
        speechRecognizer.delegate = self
        
        SFSpeechRecognizer.requestAuthorization { (authStatus) in
            
            var isButtonEnabled = false
            
            switch authStatus {
            case .authorized:
                isButtonEnabled = true
                
            case .denied:
                isButtonEnabled = false
                print("User denied access to speech recognition")
                
            case .restricted:
                isButtonEnabled = false
                print("Speech recognition restricted on this device")
                
            case .notDetermined:
                isButtonEnabled = false
                print("Speech recognition not yet authorized")
            }
            
            OperationQueue.main.addOperation() {
                self.microphoneButton.isEnabled = isButtonEnabled
            }
        }
	}

	@IBAction func microphoneTapped(_ sender: AnyObject) {
        if audioEngine.isRunning {
            audioEngine.stop()
            // text that will be uploaded
            print(textView.text)
            
            recognitionRequest?.endAudio()
            microphoneButton.isEnabled = false
            microphoneButton.setImage(UIImage(named: "mic"), for: .normal)
            // update the information in the list
            for i in 0...7 {
                if tempInformationList[i] != ""{
                    finalInformationList[i] = tempInformationList[i]
                }
            // update the textFields
            startingLocationTextField.text = finalInformationList[0]
            endingLocationTextField.text = finalInformationList[1]
            departMonthTextField.text = finalInformationList[2]
            departDayTextField.text = finalInformationList[3]
            returnMonthTextField.text = finalInformationList[4]
            returnDayTextField.text = finalInformationList[5]
            numOfPassengersTextField.text = finalInformationList[6]
            classTextField.text = finalInformationList[7]
                
            // check if all information is filled out then show the button
                var count = 0
                for i in 0...7 {
                    if finalInformationList[i] != "" {
                        count += 1
                    }
                    if count == 8 {
                        nextPageButton.isHidden = false
                    }
                }
            
            }
            
        } else {
            startRecording()
            microphoneButton.setImage(UIImage(named: "micRecording"), for: .normal)
            if let value = startingLocationTextField.text{
                if value != "" {
                    finalInformationList[0] = value
                }
            }
            if let value = endingLocationTextField.text{
                if value != "" {
                    finalInformationList[1] = value
                }
            }
            if let value = departMonthTextField.text{
                if value != "" {
                    finalInformationList[2] = value
                }
            }
            if let value = departDayTextField.text{
                if value != "" {
                    finalInformationList[3] = value
                }
            }
            if let value = returnMonthTextField.text{
                if value != "" {
                    finalInformationList[4] = value
                }
            }
            if let value = returnDayTextField.text{
                if value != "" {
                    finalInformationList[5] = value
                }
            }
            if let value = numOfPassengersTextField.text{
                if value != "" {
                    finalInformationList[6] = value
                }
            }
            if let value = classTextField.text{
                if value != "" {
                    finalInformationList[7] = value
                }
            }
            // check if all information is filled out then show the button
            var count = 0
            for i in 0...7 {
                if finalInformationList[i] != "" {
                    count += 1
                }
                if count == 8 {
                    nextPageButton.isHidden = false
                }
            }
        }
	}

    func startRecording() {
        
        if recognitionTask != nil {  //1
            recognitionTask?.cancel()
            recognitionTask = nil
        }
        
        let audioSession = AVAudioSession.sharedInstance()  //2
        do {
            try audioSession.setCategory(AVAudioSessionCategoryRecord)
            try audioSession.setMode(AVAudioSessionModeMeasurement)
            try audioSession.setActive(true, with: .notifyOthersOnDeactivation)
        } catch {
            print("audioSession properties weren't set because of an error.")
        }
        
        recognitionRequest = SFSpeechAudioBufferRecognitionRequest()  //3
        
        guard let inputNode = audioEngine.inputNode else {
            fatalError("Audio engine has no input node")
        }  //4
        
        guard let recognitionRequest = recognitionRequest else {
            fatalError("Unable to create an SFSpeechAudioBufferRecognitionRequest object")
        } //5
        
        recognitionRequest.shouldReportPartialResults = true  //6
        
        recognitionTask = speechRecognizer.recognitionTask(with: recognitionRequest, resultHandler: { (result, error) in  //7
            
            var isFinal = false  //8
            
            if result != nil {
                
                self.textView.text = result?.bestTranscription.formattedString  //9
                isFinal = (result?.isFinal)!
            }
            
            if error != nil || isFinal {  //10
                self.audioEngine.stop()
                inputNode.removeTap(onBus: 0)
                
                self.recognitionRequest = nil
                self.recognitionTask = nil
                
                self.microphoneButton.isEnabled = true
            }
        })
        
        let recordingFormat = inputNode.outputFormat(forBus: 0)  //11
        inputNode.installTap(onBus: 0, bufferSize: 1024, format: recordingFormat) { (buffer, when) in
            self.recognitionRequest?.append(buffer)
        }
        
        audioEngine.prepare()  //12
        
        do {
            try audioEngine.start()
        } catch {
            print("audioEngine couldn't start because of an error.")
        }
        
        textView.text = "Would you like to change or add more information..."
        
    }
    
    func speechRecognizer(_ speechRecognizer: SFSpeechRecognizer, availabilityDidChange available: Bool) {
        if available {
            microphoneButton.isEnabled = true
        } else {
            microphoneButton.isEnabled = false
        }
    }
}

