#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 08:25:55 2019
@author: omanshu
"""

import glob, shutil, os

srcDir = "/home/omanshu/Chrome DLs" # List of all files on this level
mvdir = "/home/omanshu/Downloads/"      # Will move all files here
file_list = glob.glob(srcDir + "/*.*")     # Read files from dir
fileDict = {}

for f in file_list:
    ext = f[f.rfind('.')+1:]    
    # rfind to find last occurrence of '.' to extract file extension
    if ext not in fileDict:
        fileDict.update({ext: list()})
    fileDict[ext].append(f)

for key in fileDict.keys():
    dest = mvdir + key + "/"
    if not os.path.isdir(dest):
        os.mkdir(dest, mode = 0o777)
    print("moving files to", dest)
    for fullFile in fileDict[key]:
        fName = fullFile[fullFile.rfind("/")+1:]
        shutil.move(fullFile, dest+fName)