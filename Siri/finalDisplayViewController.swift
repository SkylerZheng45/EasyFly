//
//  finalDisplayViewController.swift
//  Siri
//
//  Created by Skyler Zheng on 1/26/19.
//  Copyright © 2019 Sahand Edrisian. All rights reserved.
//

import UIKit

class finalDisplayViewController: UIViewController{
    var ticketInfoLast:Array<String>?
    @IBOutlet weak var displayLabel: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        let tap = UITapGestureRecognizer(target: self.view, action: #selector(UIView.endEditing(_:)))
        tap.cancelsTouchesInView = false
        self.view.addGestureRecognizer(tap)
        if let ticketInfo = ticketInfoLast{
            //edit the output things
            displayLabel.text =
            """
            \(ticketInfo[0])
            \(ticketInfo[1])
            \(ticketInfo[2])
            \(ticketInfo[3])
            """
        }
    }
    
    
}
