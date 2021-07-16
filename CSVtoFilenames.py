# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 15:06:58 2020

@author: nesib
"""

import os

path = './Resimler'
file = open('FaceTags.csv','r') 
data =file.read().split('\n')

for row in data:
    if row == "":
        break
    partial = row.split(',')
    oldname = os.path.join(path, partial[0]+'.png')
    if os.path.exists(oldname):
        newname = os.path.join(path, partial[1])
        os.rename(oldname, newname)
    else:
        print ("hata"+oldname)
file.close();