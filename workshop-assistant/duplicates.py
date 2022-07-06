
#!/usr/bin/env python
import sys
import os
import hashlib
import datetime
import re




#https://www.checkyourmath.com/convert/digital_storage/megabytes_gigabytes.php
#https://stackoverflow.com/questions/2365100/converting-bytes-to-megabytes
#https://stackoverflow.com/questions/6149006/how-to-display-a-float-with-two-decimal-places
def convertBytesToMegaBytes(bytesinput):
    someMoreMath= '%.10f' % float(bytesinput/1024/1024)
    someMoreMath= '%.8f' % float(bytesinput/1024/1024)
    return someMoreMath
def convertMBtoGB(mbInput):
    return mbInput/1024
    
def checkFileSize(fileInput):
#   file_info = os.stat(fileInput)
    #You need to have seek() in order to specify the space. I know it's strange.
    fileInput.seek(0, os.SEEK_END)
    #returns an integer value in bytes
    return(fileInput.tell())
    
#https://www.quickprogrammingtips.com/python/how-to-calculate-md5-hash-of-a-file-in-python.html
def getHashesSmall(fileInput):
    with open(fileInput,"rb") as f:
        bytes = f.read() # read file as bytes
        readable_hash = hashlib.md5(bytes).hexdigest();
    return(readable_hash)
    
def getHashesLarge(fileInput):
    with open(fileInput,"rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            hashlib.md5().update(byte_block)
    return(hashlib.md5().hexdigest())

def compareHashes(fileInputA, fileInputB):
    return 0;



def checkForDuplicatesInOneFile(arrayInput):
    counter = 0
    counterb = 0
    listofdupes = []
    for i in range(counter, len(arrayInput), 1):
        # print("i is %s" % (i))
        # print("counter i is %s" % (arrayInput[i]))
        for j in range(counterb, len(arrayInput), 1):
            # print("j is %s" % (j))
            # print("counter j is %s" % (arrayInput[j]))
            if (arrayInput[i] == arrayInput[j] and i != j):
                listofdupes.append(arrayInput[i])
    # print("check work")
    if(len(listofdupes)>0):
        print("The file contained duplicates:::\n")
    else:
        print("File had no duplicates")
    return(listofdupes)
    
def sortAndRemoveDuplicates(fileInput):
        #store these in an array
        
        lines = fileInput.readlines()

        #https://stackoverflow.com/questions/3951547/java-array-finding-duplicates
        #presort check:
        print("pre sort check")

        for i in lines:
            print(i)
        print("\n\nChecking For duplicates in the file....\n\n")
    
        lines.sort()
        #postsort check
        print("post sort check")
        for i in lines:
            print(i)

        print("Obtaining Elements to Remove...\n")
        listofdupes=[]
        listofdupes = checkForDuplicatesInOneFile(lines)
        for i in listofdupes:
            print(i)
        pruned_lines = list(set(lines))
        print("\nThe original size of the file was ", len(lines))
        print("The pruned size of the file is ", len((pruned_lines)))
        return(pruned_lines)
        
def generateCleanedFile(arrayInput):
    timestamp = datetime.datetime.utcnow()
    fileName = str(timestamp) + "cleaned.txt"
    arrayInput.sort()
    
    with open(fileName, 'w') as newFile:
        for i in arrayInput:
            print("adding I: ", i)
            newFile.write(i)
        newFileSize = checkFileSize(newFile)
    newFile.close()
    return newFileSize


def createDictionary(fileInput):
    #fileInput is sys.argv[1]
#    stringexample="zone \"domana2.com\" IN { type master; file \"sinkhole-drive-by.db\"; };"
#    print(re.findall(r'"(.*?)"', stringexample))
    dictionaryOutput = {}
    lines = fileInput.readlines()
    for i in lines:
        regexresults=re.findall(r'"(.*?)"', i)
        try:
            domain = regexresults[0]
            category =  regexresults[1]
            dictionaryOutput[domain] = category
        except:
            
            print("unable to add: ", i)
    for i in dictionaryOutput:
        ## I guess the dictionary key will just take on the most recent value
        print(i)
        print(dictionaryOutput[i])
    return(dictionaryOutput)
        


    
def identifyDuplicateDomains(dictionaryInput):
#https://stackoverflow.com/questions/171480/regex-grabbing-values-between-quotation-marks
    stringexample="zone \"domana2.com\" IN { type master; file \"sinkhole-drive-by.db\"; };"
    print(re.findall(r'"(.*?)"'),stringexample)
#https://thispointer.com/can-a-dictionary-have-duplicate-keys-in-python/
    duplicatevalDictionary = {}
    return duplicatevalDictionary


def main():
        ###########################################################################
        # 1. Get User Input
        ###########################################################################
        dialogBoxInput=''
        dialogBoxInput=input('\nOffset of lines?\n')
        if(dialogBoxInput==''):
            dialogBoxInput=0
        dialogBoxInput=int(dialogBoxInput)
        
        ###########################################################################
        # 2. Open file
        ###########################################################################
        f = open(sys.argv[1], 'r')
        createDictionary(f)

        
        ###########################################################################
        # 3. Get File Stats
        ###########################################################################
        FileSizeBytes = checkFileSize(f)
        FileSizeMegabytes = float(convertBytesToMegaBytes(FileSizeBytes))
        print("Size of file is:", FileSizeMegabytes, "megabytes")
        
        
        print("Md5 hash (small method): ", getHashesSmall(sys.argv[1]))
        print("Md5 hash (large method): ", getHashesLarge(sys.argv[1]))

        ###########################################################################
        # 4. Start cleaning by sorting and removing duplicates + making a new file
        ###########################################################################
#        f = open(sys.argv[1], 'r')
#        cleanedArray = sortAndRemoveDuplicates(f)
#        newFileSize = generateCleanedFile(cleanedArray)
#
#
#        #5 Compare the two files
#        print("Old File Size: ", checkFileSize(f), " bytes")
#        print("New File Size: ", newFileSize, " bytes")
#
#        f.close()
#        identifyDuplicateDomains(dictionaryinput)
            
        f.close()



if __name__ == "__main__":
        main()

