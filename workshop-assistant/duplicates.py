

#!/usr/bin/env python
import sys
import os

def checkFileSizes(fileA, fileB):
    print(os.stat(fileA))
    print(os.stat(fileB))
    
    


def main():
        dialogBoxInput=''
        dialogBoxInput=input('\nOffset of lines?\n')
        if(dialogBoxInput==''):
            dialogBoxInput=0
        dialogBoxInput=int(dialogBoxInput)
            
            
            
        with open(sys.argv[1], encoding='utf8') as f:
                lines=f.readlines()

        
        arraylen=len(lines)
        
        counterA=1-dialogBoxInput;
        
        counterB=0
        
  
#
#        for i in lines:
#            counterA+=1
#            print("\n%s Corresponds to the content %s" % (counterA, i))
#            for j in lines:
#                counterB+=1
#                if(i==j):
#                    print("duplicate found!!! at line i %s, line j %s \t value is %s vs %s" % (counterA, counterB, i, j))

        stringarrayexample=['a', 'b' ,'c', 'd', 'a', 'f']
#
#        for i in lines:
#            print(type(i))
#            print(i)
#            for j in stringarrayexample:
#                print(type(j))
#                print(j)
#                if(i==j):
#                    print("duplicate found")
#        print(stringarrayexample[1])
#        print(stringarrayexample[0])
        counter=0
#        for i in range(counter, len(stringarrayexample), 1):
#            print(counter)
#            print(stringarrayexample[counter])
#            try:
#                print(stringarrayexample[counter+1])
#
#            except:
#                print("end of index")
#            counter+=1;
#






#https://stackoverflow.com/questions/3951547/java-array-finding-duplicates
        listofdupes=[]
        counterb=counter+1
        i=0
        j=0

        for i in range(counter, len(stringarrayexample), 1):
            print("i is %s" % (i))
#            print("counter is %s" % (counter))
#            print("counter index is %s" % (stringarrayexample[counter]))
            print("counter i is %s" % (stringarrayexample[i]))
#            counter+=1
            for j in range(counterb, len(stringarrayexample), 1):
                print("j is %s" % (j))
#                print("counterb is %s" % (counterb))
#                print("counter index value is %s" % stringarrayexample[counterb] )
                print("counter j is %s" % (stringarrayexample[j]))
                if(stringarrayexample[i]==stringarrayexample[j] and i!=j):
                    print("DUPLICATE FOUND!!!!!!!!!!!!!!!!!!!!!! at this value %s" % stringarrayexample[i] )
                    listofdupes.append(stringarrayexample[i])
#                if(stringarrayexample[counter]==stringarrayexample[counterb]):
#                    print("duplicate found")
#                    counter+=1
            print("check work")
            print(listofdupes)
#
#        for i in range(len(stringarrayexample)):
#            print(i)
#            print(stringarrayexample.index(i))
            #print(stringarrayexample[])
            
            
        f.close()




if __name__ == "__main__":
        main()

