# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 16:07:43 2021

@author: secretaria
"""

import os
path = 'C:/Program Files (x86)/Microsoft Office/'
path_office = None

for root, dirs, files in os.walk(path, topdown=True):
    #print(root)
    if root[len(path):].find('Office') != -1:
        path_office = root
        print(path_office)
        break
    #print(files)
'''
from sys import platform
if platform == "linux" or platform == "linux2":
    # linux
    super
if platform == "darwin":
    # OS X
    print('OS X')
elif platform == "win32":
    print('wind32')

import subprocess
#subprocess.call("echo Hello World", shell=True) 
subprocess.call(path_office+ "/WINWORD.EXE --WRITER database/imported_documents/testttt2.docx")
'''
DETACHED_PROCESS = 0x000008
import subprocess
pid = subprocess.Popen(["C:/Program Files (x86)/Microsoft Office/Office15/WINWORD.EXE","database/imported_documents/testttt2.docx"]).pid