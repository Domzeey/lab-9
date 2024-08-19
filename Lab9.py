#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:46:59 2023

@author: dominion
"""

import os

print (os.getcwd())

def create_new_file():
    file_name = "second_python_file.txt"
    file_path = "\\Users\\dominion\\Documents\\CMP7244\\Lab9"
    
    file = open(file_name, "w")
    
    file.write("my name is dominion\n")
    
    file.close()

create_new_file()