"""
Description: Module 2 Assignment Data Types
Author:Tyler Jablonski
Date: Sept 18 2024
"""

#SIMPLE DATA TYPES
name = "Tyler"
print("value:",name)
print("type:",type(name))

LicenseStatus = True
print("value:",LicenseStatus)
print("type:",type(LicenseStatus))

year = 2024
print("value:",year)
print("type:",type(year))
year +=1
print("value:",year)
print("type:",type(year))
#CALCULATIONS
GST = .05
PST =  .07
Price  = 70000

FederalTax = Price *  GST

provincialTax = Price *  PST
FinalCost = Price  + FederalTax + provincialTax

print("Pre-Tax Value:", Price, "Provincial Tax: ",provincialTax, "Federal Tax: ",  FederalTax, "Final Cost: ", FinalCost)
Text = f" Pre-Tax Value: ${Price:,.2f} Provincial Tax: ${provincialTax:,.2f} Federal Tax: ${FederalTax:,.2f} total:  ${FinalCost:,.2f}"
print(Text)

#LISTS
Numbers = [1,2,3,4,5,6,7,8,9,10]
print(type(Numbers))
print(Numbers)

Numbers.insert(5,"Tyler")
print(Numbers)

Numbers.remove(9)
print(Numbers)

list2 = ["A","B","C"]

list3 = Numbers + list2
print(list3)
#TUPLES
provinces  = ("BC","Alberta","Ontario","Manitoba")
print(type(provinces))
print(provinces)

#DICTIONARIES
Coins = {
    "quarter": 0.25,
    "nickel": 0.05,
    "dime": 0.10
}
print(type(Coins))
print(Coins)
Coins["Loonie"] =  1.00
Coins["Toonie"] = 2.00
print(Coins)
#SETS
EvenNumbers = {
    2,4,6,8,10,12,14,16,18,20
}
print(type(EvenNumbers))
print(EvenNumbers)

MultiplesOf5 = {
    5,10,15,20
}
print(MultiplesOf5)

EvensAndMultiples = EvenNumbers.union(MultiplesOf5)
print(EvensAndMultiples)

CommonMultiples =  EvenNumbers.intersection(MultiplesOf5)
print(CommonMultiples)

EvenDifferences =   EvenNumbers.difference(MultiplesOf5)
print(EvenDifferences)
MultiplesOf5Differences =  MultiplesOf5.difference(EvenNumbers)
print(MultiplesOf5Differences)




