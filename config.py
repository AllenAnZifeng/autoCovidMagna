#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: config.py
@time: 2020/8/21 14:03
'''
import os
ChromeDriverPath = os.path.join(os.path.dirname(os.path.realpath(__file__)),"chromedriver.exe")

INFORMATION = {'firstname': '', 'lastname': '', 'phone': '','email':''}
EMAIL = 'covidAutoCheckin@gmail.com'
PASSWORD = 'u,Nzr}M"J9[/89t['

with open('info.txt', 'r') as f:
    temp = []
    counter = 0
    for line in f.readlines():
        temp.append(line.rstrip())
    for key in INFORMATION.keys():
        INFORMATION[key] = temp[counter]
        counter += 1


