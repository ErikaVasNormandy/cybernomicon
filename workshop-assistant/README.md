# Price Calculator

**When you just want to know how much a cup of flour costs**

How to use:

python pricecalculator.py

**Tags:** basic python review, integer formatting, decimal formatting, bold terminal output, while loops, input dialog boxes

**Section 1: Prompt user for type of bulk item**
Initiates the **while True:** loop where the user simply goes to a directory of bulk items

bulkInput=input("\nMake a selection below [enter]:\nProgram will default to [1] Flour if none are chosen\n[1] Flour\n[2] Rice\n[3] Oats\n[4] Sugar\n[5] Pasta\n[6] Lentils\n[7] Milk\n[8] Eggs\n\n")


**Section 2: Prompt user for how many cups**
while(dialogBoxInput==''):
dialogBoxInput=input('\nHow many cups of %s are required?\n' % itemDictionary[bulkInput])


**Section 3: Calculate **
First part is mainly Volume, second part is mainly Mass


