#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 17:27:12 2018

@author: dillon
"""

import os

# just variables to turn stuff on and off
testing = False
training = True
classify = False
display_results = False
# current nurl networks, AlexNet,LeNet
currentNetwork = "AlexNet"
# list for instrument catigoryies
# As ashamed as I am to admit this, I feel that you're more qualified to edit this than I am ~Dillon
catigoryies = ["drums","base","keyboard","voice"]

# names of folders for training and testing
traingFolder = "./training"
testingFolder = "./testing" 