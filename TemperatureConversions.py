#CS175L
#Delvis Rodriguez
#Temperature Conversions

def main():
    controlLoop()

def convertToKelvin(fahrenheit):
    Kelvin = float((((fahrenheit - 32) * 5) / 9) + 273.15)
    return Kelvin

def convertToCentigrade(Fahrenheit):
    Centigrade = float((5 / 9 * (Fahrenheit - 32)))
    return Centigrade

def doConversion():
    Fahrenheit = float(getFahrenheit())
    Kelvin = float(convertToKelvin(Fahrenheit))
    Celsius = float(convertToCentigrade(Fahrenheit))
    print(f'Fahrenheit: {Fahrenheit:.2f} Kelvin: {Kelvin:.2f} Centigrade: {Celsius:.2f}')
    print(f'Exiting the program')

def repeat():
    while True:
        try:
            Conversions = int(input('How many conversions would you like to do this time? '))
            for how_many in range(1, Conversions + 1):
                doConversion()
            break  
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def controlLoop():
    while True:
        try:
            Conversions = str(input('Do you want to do some conversions(Yes or No)? ')).capitalize()
            if Conversions == 'Yes':
                repeat()
                break
            elif Conversions == 'No':
                print('Exiting the program')
                break
            else:
                raise ValueError('Invalid input. Please enter either Yes or No.')
        except ValueError as e:
            print(e)
        
def getFahrenheit():
    while True:
        try:
            Fahrenheit = float(input('Enter Fahrenheit temperature (must be -50 to 130): '))
            while (Fahrenheit < -50) or (Fahrenheit > 130):
                print('Invalid input. Enter a valid value between -50 and 130.')
                Fahrenheit = float(input('Enter Fahrenheit temperature (must be -50 to 130): '))
            return Fahrenheit
        except ValueError:
            print('Invalid input. Please enter a number.')

# This code will call the 'main' function if the entire program was run.
if __name__ == '__main__':
    main()
