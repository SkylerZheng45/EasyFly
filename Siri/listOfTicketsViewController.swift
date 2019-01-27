//
//  listOfTicketsViewController.swift
//  Siri
//
//  Created by Skyler Zheng on 1/26/19.
//  Copyright © 2019 Sahand Edrisian. All rights reserved.
//

import UIKit
import Firebase
import FirebaseDatabase

class listOfTicketsViewController: UIViewController, UITableViewDelegate, UITableViewDataSource {
    
    var ticketList = ["$100    AA342   AirbusA370","Departure time: 8:00AM","Arrival time: 4PM","Duration: 8 hours","$150    AA2643   Boeing747","Departure time: 6:00AM","Arrival time: 5PM","Duration: 9 hours","230    AA846   Boeing787","Departure time: 4:00AM","Arrival time: 13AM","Duration: 9 hours","","","","","","","","","","","","","","","","","","",]
    var ticketInfo = ""
    var ref: DatabaseReference!
    var databaseHandle:DatabaseHandle?
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return(ticketList.count)
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = UITableViewCell(style: UITableViewCellStyle.default, reuseIdentifier: "cell")
        cell.textLabel?.numberOfLines = 0;
        cell.textLabel?.text = ticketList[indexPath.row]
        return cell
    }
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        ticketInfo = ticketList[indexPath.row]
        performSegue(withIdentifier: "showFinalPage", sender: [ticketList[indexPath.row],ticketList[indexPath.row+1],ticketList[indexPath.row+2],ticketList[indexPath.row+3]])
    }
   
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
            if let viewEdit = segue.destination as? finalDisplayViewController{
                viewEdit.ticketInfoLast = sender as? Array
            }

    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        let tap = UITapGestureRecognizer(target: self.view, action: #selector(UIView.endEditing(_:)))
        tap.cancelsTouchesInView = false
        self.view.addGestureRecognizer(tap)
        
         ref = Database.database().reference()
//
//        databaseHandle = ref.observe(DataEventType.value, with: { (snapshot) in
//            let postDict = snapshot.value as? [String : String] ?? [:]
//            var tickets:[String] = []
//            var count = 1
//            for (name, info) in postDict{
//                if name == "ticketInfo" + String(count) + String(1){
//                    tickets.append(info)
//                    count+=1
//                }
//            }
//            self.ticketList = tickets
//        })
    }
    
    
}
