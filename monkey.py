# -*- coding: utf-8 -*-
# python

# a script to convert file encoding

import os

#inputDir = '/Users/t/web/p/monkey_king'
inputDir = 'file://home/arungaya/monkey.html'

def changeEncoding(filePath):
    '''take a full path to a file as input, and change its encoding from gb18030 to utf-16'''
    print filePath

    tempName = filePath+'~-~'

    inputFile = open(filePath,'rb')
    content = unicode(inputFile.read(),'gb18030')
    inputFile.close()

    outputFile = open(tempName,'wb')
    outputFile.write(content.encode('utf-16'))
    outputFile.close()

    os.rename(tempName,filePath)

def fileFilter(dummyArg, thisDir, dirChildrenList):
    for child in dirChildrenList:
        if '.html' == os.path.splitext(child)[1] and os.path.isfile(thisDir+'/'+child):
            changeEncoding(thisDir+'/'+child)
os.path.walk(inputDir, fileFilter, None)