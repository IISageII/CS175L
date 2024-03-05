#CS175L
#Delvis Rodriguez
#Temperature Conversions
def main():
    controlLoop()

def convertToKelvin(fahrenheit):
    Kelvin = (fahrenheit - 32) * 5 / 9 + 273.15
    return Kelvin

def convertToCentigrade(Fahrenheit):
    Centigrade = (5 / 9 * (Fahrenheit - 32))
    return Centigrade

def doConversion():
    Fahrenheit = getFahrenheit()
    Kelvin = convertToKelvin(Fahrenheit)
    Celsius = convertToCentigrade(Fahrenheit)
    print(f'Fahrenheit: {Fahrenheit:.2f} Kelvin: {Kelvin:.2f} Centigrade: {Celsius:.2f}') 

def repeat():
    Conversions = int(input('How many conversions would you like to do this time? '))
    for how_many in range(1, Conversions + 1):
        doConversion()

def controlLoop():
    Conversions = input('Do you want to do some conversions(Yes or No)? ')
    if Conversions.capitalize() == 'Yes':
        repeat()
        
def getFahrenheit():
    Fahrenheit = float(input('Enter Fahrenheit temperature (must be -50 to 130): '))
    while (Fahrenheit < -50) or (Fahrenheit > 130):
        Fahrenheit = float(input('Please re-enter '))
    return Fahrenheit


# This code will call the 'main' function if the entire program was run.
if __name__ == '__main__':
    main()
