#!/usr/bin/env python.
import sys


def convertPoundsToKilos(poundsInput):
	Kilos = float(poundsInput) / 2.2
	return Kilos;

def convertPoundsToCups(poundsInput, typeInput):
	typeOutput=int()
	if(typeInput==1):
		#flour
		#print("1 pound of flour is 3.343 cups")
		typeOutput=3.334
	if(typeInput==2):
		#rice
		#print("1 pound of rice is 2.5 cups")
		typeOutput=2.5
	if(typeInput==3):
		#print("8 oz weight of oats is 2.5 cups, measured this actually. Also 2.625 pounds is apparently 13.125 cups")
		#oats
		typeOutput=5.04
	cups = float(poundsInput) * typeOutput
	return cups;



def convertPoundsToDollars(poundsInput, typeInput):
	typeOutput=int()
	if(typeInput==1):
		#flour
		#print("poundstodollars flour... 5 pounds for 3 dollars")
		typeOutput=.6
	if(typeInput==2):
		#print("poundstodollars rice... 15 pounds for 31.69 dollars")
		#rice
		typeOutput=2.12
	if(typeInput==3):
		#oats
		typeOutput=1.253
	Dollars = float(poundsInput) * typeOutput
	return Dollars;

#my heart is filled with some pretty dark thoughts these days


def convertCupsToDollars(cupsInput, typeInput):
	typeOutput=int()
	if(typeInput==1):
		#flour 3.343 cups is .6 dollars.... .179 dollars
		typeOutput=.18
	if(typeInput==2):
		#rice  2.5 cups is 2.112 dollars, so that is 1.056 dollars per 1 cup
		typeOutput=1.056
	if(typeInput==3):
		#contentious oats $.248 per cup of oats
		#13.125 cups per 3.29>???
		typeOutput= .25
	#rounded this one up because inflation :/
	Dollars = float(cupsInput) * typeOutput
	return Dollars;

def convertCupsToPounds(cupsInput, typeInput):
	typeOutput=float()
	if(typeInput==1):
		#flour 1 cup should be .3 pounds
		typeOutput=.3125
	if(typeInput==2):
		#rice
		#print("rice cups to pounds, .4 pounds for every cup?")
		typeOutput=.41
	if(typeInput==3):
		#oats
		#print("oats are apparently .2 pounds per cup")
		typeOutput=.2
	pounds=float(cupsInput) * typeOutput
	#pounds = round(float(cupsInput)*typeOutput, 2)
	return pounds

def convertCupsToGrams(cupsInput, typeInput):
	typeOutput=int()
	if(typeInput==1):
		#1 cup of flour is 120 grams
		typeOutput=120
	if(typeInput==2):
		#1 cup of rice is 210 grams
		typeOutput=210
	if(typeInput==3):
		#1 cup of oats is 80 grams
		typeOutput=80
	grams = cupsInput*typeOutput
	return grams

def convertCupsToFlOZ(cupsInput, typeInput):
	typeOutput=int()
	if(typeInput==1):
		#flour
		typeOutput=3.62
	if(typeInput==2):
		#rice
		typeOutput=2.5
	if(typeInput==3):
		#oats
		typeOutput=2.5
	floz = cupsInput*8
	return floz

def convertPoundsToGrams(poundsInput, typeInput):
	typeOutput=int()
	if(typeInput==1):
		#flour
		typeOutput=453.592
	if(typeInput==2):
		#rice
		typeOutput=453.59
	if(typeInput==3):
		#oats
		typeOutput=2.5
	grams = poundsInput*typeOutput
	return grams



def main():


	try:
		while True:
			print("\n----------------------\nPrice Calculator\n----------------------\n")


			# 1. Choose Bulk Item
			bulkInput=input("\nMake a selection below [enter]:\nProgram will default to [1] Flour if none are chosen\n[1] Flour\n[2] Rice\n[3] Oats\n[4] Milk\n\n")
			bulkInput=int(bulkInput)
			itemDictionary = {
				1: "Flour",
				2: "Rice",
				3: "Oats",
				4: "Milk",
				5: "Pasta",
				6: "Lentils"
			}

			print("\nYou Chose [%s], aka %s. Keep in mind that these are approximate measurements only" % (bulkInput, itemDictionary[bulkInput]))


			# 2. Prompt user for how many cups
				# returns string or None without the int() function
			dialogBoxInput=''
			while(dialogBoxInput==''):
				dialogBoxInput=input('\nHow many cups of %s are required?\n' % itemDictionary[bulkInput])
				#if(dialogBoxInputpyautogui.alert("Please enter a number")
			dialogBoxInput=int(dialogBoxInput)

			# 3. Calculate
			print("\n------------------------Volume------------------------\n")
			print("%s cup(s) of %s would be \n\t\033[96m %s dollars \033[0m " % (dialogBoxInput, itemDictionary[bulkInput], convertCupsToDollars(dialogBoxInput, bulkInput)));
			print("\t\033[96m %s pounds \033[0m" % (convertCupsToPounds(dialogBoxInput, bulkInput))); 
			print("\t\033[96m %s grams \033[0m " % (convertCupsToGrams(dialogBoxInput, bulkInput)))


			print("\n------------------------Mass------------------------\n")
			print("%s pound(s) of %s would be \n\t\033[96m %s dollars \033[0m " % (dialogBoxInput, itemDictionary[bulkInput], convertPoundsToDollars(dialogBoxInput, bulkInput)));
			print("\t\033[96m %s cups \033[0m" % (convertPoundsToCups(dialogBoxInput, bulkInput)));

			print("\n\n----------------------start over----------------------\n")
			
	except KeyboardInterrupt:
		print('\n\tinterrupted!\t\n')

#we'll take in a number, and calcuate the price
#We have a cup of flour, that is ___ dollars

if __name__ == "__main__":
	main()
	
