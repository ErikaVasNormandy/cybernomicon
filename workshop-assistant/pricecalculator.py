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
	if(typeInput==4):
		#sugar
		typeOutput=5.1
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

def simpleEggMath(packagetype, cost):
	return cost / packagetype
	#return cost * howManyEggs / packagetype

def butterAndMargarine(butterUsedInput, packageAmount, butterprice):
	unitOfConversion = butterprice/packageAmount
	print("\n\033[96m%.2f\033[0m per individual stick of butter, (\033[96m%.2f \033[0m per tablespoon)" % (unitOfConversion, unitOfConversion/8))
	totalcost = unitOfConversion*butterUsedInput
	return(totalcost)



# def butterAndMargarine(typeInput, amountused, packageAmount, inputPrice):
# 	print("\nRemember:: \n1 Stick of butter/margarine == 8 tbsps \n1 Stick of butter == 1/2 a cup\n ")
# 	if(typeInput=='1'):
# 		#sticks
# 		conversionFactor = inputPrice/packageAmount
# 		print("\n%.4f per individual stick at %s dollars\n" % (conversionFactor, inputPrice ))
# 		print("%.2f for this recipe if it called for %s sticks of butter and you bought it at %s" % (conversionFactor*amountused , amountused, inputPrice))
# 		if(typeInput=='2'):
# 		#cups
# 		conversionFactor = inputPrice/packageAmount
# 		print("\n%.4f per individual stick at %s dollars\n" % (conversionFactor, inputPrice ))
# 		print("%.2f for this recipe if it called for %s sticks of butter and you bought it at %s" % (conversionFactor*amountused , amountused, inputPrice))
	



def main():
	itemDictionary = {
		1: "Flour",
		2: "Rice",
		3: "Oats",
		4: "Sugar",
		5: "Pasta",
		6: "Lentils",
		7: "Milk",
		8: "Eggs",
		9: "Butter",
	}

	try:
		while True:
			print("\n------------------------------------------------------------------\n\033[96m BASIC PRICE CALCULATOR\033[0m \n------------------------------------------------------------------\n")

######################################
			# 1. Choose Bulk Item
######################################

			bulkInput=input("Make a selection below [enter]:\nProgram will default to [1] Flour if none are chosen\n\n[1] Flour\n[2] Rice\n[3] Oats\n[4] Sugar\n[5] Pasta\n[6] Lentils\n[7] Milk\n[8] Eggs \n[9] Butter\n\n")
			bulkInput=int(bulkInput)

	
			print("\nYou Chose [%s], aka %s. Keep in mind that these are approximate measurements only" % (bulkInput, itemDictionary[bulkInput]))

######################################
			# 2. Prompt user for How Many Cups
######################################
			# returns string or None without the int() function

######################################
			# 2.5 Handle Special Cases like eggs and butter
######################################

			if(itemDictionary[bulkInput])=="Eggs":
				print("For example, if a dozen pack of eggs is 2.99, one egg is going to be roughly 3 / dozen == 3 / 12 == $0.25 an egg")

				#call function for eggs
				eggPackageCount=''
				while(eggPackageCount==''):
					eggPackageCount=input("Did you buy a dozen? The 18-pack?\n")
				eggPackageCount=int(eggPackageCount)

				# howManyEggs=''
				# while(howManyEggs==''):
				# 	howManyEggs=input("How many eggs are you using?")
				# howManyEggs=int(howManyEggs)

				eggprice=''
				while(eggprice==''):
					eggprice=input("How much did you pay?\n")
				eggprice=float(eggprice)

				eggCostUnit = simpleEggMath(eggPackageCount, eggprice)

				print("\nA %s pack of eggs at \033[96m%s\033[0m would be\033[96m %.2f\033[0m per egg\n" % (eggPackageCount, eggprice,  eggCostUnit))
				print("For example, \n2 eggs --> \033[96m$%.2f\033[0m \n4 eggs --> \033[96m$%.2f\033[0m \n8 eggs --> \033[96m$%.2f\033[0m\n" % (eggCostUnit*2, eggCostUnit*4, eggCostUnit*8))

			elif(itemDictionary[bulkInput])=="Butter":
#def butterAndMargarine(amountused, packageAmount, inputPrice):
				# measurementType=input("Sticks? Cups? Tablespoons? \n1) Sticks \n2) Cups\n3) Tablepoons\n\n")
				butterUsedInput=''
				while(butterUsedInput==''):
					butterUsedInput=input("Sticks Used? (8 tbsps in a stick)\n")
				butterUsedInput=int(butterUsedInput)

				butterprice=''
				while(butterprice==''):
					butterprice=input("How much did you pay?\n")
				butterprice=float(butterprice)

				packageAmount=''
				while(packageAmount==''):
					packageAmount=input("Quantity of the package?\n")
				packageAmount=int(packageAmount)

				cost = butterAndMargarine(butterUsedInput, packageAmount, butterprice)
				print("\nUsing \033[96m%s stick(s) (8 tbsps)\033[0m of butter, at \033[96m%.2f\033[0m for a \033[96m%s stick\033[0m container\n" % (butterUsedInput, butterprice, packageAmount) )
				print("It would cost you \033[96%s\033[0m total" % (butterAndMargarine(butterUsedInput, packageAmount, butterprice)))

				# butterAndMargarine(measurementType, butterUsedInput, packageInput, butterprice)



			# elif(itemDictionary[bulkInput])=="Margarine":
			# 	print("For example, if a dozen pack of eggs is 2.99, one egg is going to be roughly 3 / dozen == 3 / 12 == $0.25 an egg")

			# 	#call function for eggs
			# 	eggPackageCount=''
			# 	while(eggPackageCount==''):
			# 		eggPackageCount=input("Did you buy a dozen? The 18-pack?\n")
			# 	eggPackageCount=int(eggPackageCount)

			# 	eggprice=''
			# 	while(eggprice==''):
			# 		eggprice=input("How much did you pay?\n")
			# 	eggprice=float(eggprice)

			# 	butterAndMargarine(butterInput, butterprice)


######################################
			# 3. Calculate conventional bulk prices
######################################
			else:
				dialogBoxInput=''
				while(dialogBoxInput==''):
					dialogBoxInput=input('\nHow many cups of %s are required?\n' % itemDictionary[bulkInput])
					#if(dialogBoxInputpyautogui.alert("Please enter a number")
				dialogBoxInput=int(dialogBoxInput)

				print("\n------------------------------------------------------------------\nVolume\n------------------------------------------------------------------\n")
				print("%s cup(s) of %s would be \n\t\033[96m %.2f dollars \033[0m " % (dialogBoxInput, itemDictionary[bulkInput], convertCupsToDollars(dialogBoxInput, bulkInput)));
				print("\t\033[96m %.3f pounds \033[0m" % (convertCupsToPounds(dialogBoxInput, bulkInput))); 
				print("\t\033[96m %s grams \033[0m " % (convertCupsToGrams(dialogBoxInput, bulkInput)))

				print("\n------------------------------------------------------------------\nMass\n------------------------------------------------------------------\n")
				print("%s pound(s) of %s would be \n\t\033[96m %s dollars \033[0m " % (dialogBoxInput, itemDictionary[bulkInput], convertPoundsToDollars(dialogBoxInput, bulkInput)));
				print("\t\033[96m %s cups \033[0m" % (convertPoundsToCups(dialogBoxInput, bulkInput)));
                
	except KeyboardInterrupt:
		print('\n\tinterrupted!\t\n')

#we'll take in a number, and calcuate the price
#We have a cup of flour, that is ___ dollars

if __name__ == "__main__":
	main()
	
