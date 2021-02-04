"""
Class: CS602-GC1
Name: Lily Sunil Karmakar
Description: (Programming Project: Jet Fuel)

By submitting this assignment, I certify that:
I have completed this programming assignment independently.
I have not copied the code from a student or any source.
I have not shared my code with any student.

"""
print (f"""This program takes the amount of Jet A fuel in gallons and calculates
the following:""")
print("""
      1. Equivalent number of liters
      2. Number of barrels of oil required
      3. Pounds of Carbon Dioxide produced
      4. BTUs produced
      5. Weight in pounds
      6. Total price in US dollars
      7. Flight time of a 767
""")
#Named_constants
LTR  = 3.7854
BAR  = 4
CO2  = 21.095
BTU  = 128100
WEI  = 6.7
COST = 4.48
HOUR = 1279

jet_fuel = float(input('Please enter the number gallons of Jet A fuel you wish to purchase :'))
jet_fuel = round(jet_fuel,2)
print('------')
print(f'Original number of gallons is: {jet_fuel:,.2f}')

#convert into Lts
ltr = jet_fuel*LTR
print(f'{jet_fuel:,} gallons of Jet A fuel is equivalent of {ltr :,.2f} Liters')

#gallon into barrels
barrel = jet_fuel/BAR
print(f'{jet_fuel:,} gallons of Jet A fuel requires {barrel:,.2f} barrels of oil')

#1 gallon of Jet A fuel produces approximately 21.095 pounds of CO2.
co2 = jet_fuel*CO2
print(f'{jet_fuel:,} gallons of Jet A fuel produces {co2 :,.2F} pounds of CO2')

#1 gallon of Jet A fuel produces 128,100 BTUs.
btu = jet_fuel*BTU
print(f"""{jet_fuel:,} gallons of Jet A fuel produces {btu :,.2f} BTUs of 
energy""")

#1 gallon of Jet A fuel weighs 6.7 pounds 
wei = jet_fuel*WEI
print(f'{jet_fuel:,} gallons of Jet A fuel weight {wei:,.2f} Pounds')

#The average price for a gallon of Jet A fuel is $4.48/gallon.
cost =jet_fuel*COST
print(f'{jet_fuel:,} gallons of Jet A fuel costs {cost :,.2f}')

#A 767 aircraft burns 1279 gallons of Jet A fuel per hour.
hr_timing = jet_fuel//HOUR
mn = round((jet_fuel/HOUR)*60)
mn_timing = mn%60
print ('------')
print(f'Total flight time of a 767 aircraft: {hr_timing:.0f} Hours {mn_timing:02} Minutes')
        


