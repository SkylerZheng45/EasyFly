//
//  finalDisplayViewController.swift
//  Siri
//
//  Created by Skyler Zheng on 1/26/19.
//  Copyright © 2019 Sahand Edrisian. All rights reserved.
//

import UIKit

class finalDisplayViewController: UIViewController{
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        let tap = UITapGestureRecognizer(target: self.view, action: #selector(UIView.endEditing(_:)))
        tap.cancelsTouchesInView = false
        self.view.addGestureRecognizer(tap)
    }
    
    
}
