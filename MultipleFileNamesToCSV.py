# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 12:02:41 2020

@author: nesib
"""


import os

path = './resimler'

i=0
file= open('./FileNames.csv', 'w')
for root, dirs, files in os.walk(path):
    for filename in files:
        i=i+1
        
        os.rename(os.path.join(path,filename), os.path.join(path,str(i)+'.png'))
        j=0
        names = filename.split('_')
        renamed=""
        for name in names:
            if len(names)-1 != j: 
                renamed+= name+"_"
            else:
                renamed+="bma1"+str(i)+".png"
            j+=1
        file.write(str(i)+","+renamed+"\n")
file.close()        
