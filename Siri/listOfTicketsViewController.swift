//
//  listOfTicketsViewController.swift
//  Siri
//
//  Created by Skyler Zheng on 1/26/19.
//  Copyright © 2019 Sahand Edrisian. All rights reserved.
//

import UIKit

class listOfTicketsViewController: UIViewController, UITableViewDelegate, UITableViewDataSource {
    
    let ticketList = [["DFW airport","Shanghai airport","$ 1000"], ["NYC Airport","Seattle Airport","$ 300"]]
    var ticketInfo = ["Error"]
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return(ticketList.count)
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = UITableViewCell(style: UITableViewCellStyle.default, reuseIdentifier: "cell")
        cell.textLabel?.numberOfLines = 0;
        cell.textLabel?.text = ticketList[indexPath.row][0]+" --> "+ticketList[indexPath.row][1]+"  \nPrice: " + ticketList[indexPath.row][2]
        return cell
    }
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        ticketInfo = ticketList[indexPath.row]
        performSegue(withIdentifier: "showFinalPage", sender: ticketInfo)
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
    }
    
    
}
