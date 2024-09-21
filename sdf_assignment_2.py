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
text = f" Pre-Tax Value: ${Price:,.2f} Provincial Tax: ${provincialTax:,.2f} Federal Tax: ${FederalTax:,.2f} total:  ${FinalCost:,.2f}"
print(text)

#LISTS

#TUPLES

#DICTIONARIES

#SETS

