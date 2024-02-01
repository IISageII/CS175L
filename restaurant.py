#CS175L
#Delvis Rodriguez
#restaurant

#Inputs:
vegetarian = str(input('Is anyone in your party vegetarian? '))
vegan = str(input('Is anyone in your party vegan? '))
gluten_free = str(input('Is anyone in your party gluten-free? '))

#Capitalizing:
vegetarian = vegetarian.capitalize()
vegan = vegan.capitalize()
gluten_free = gluten_free.capitalize()

#Boolean statements:
if vegetarian == 'Yes':
    vegetarian = True
else:
    vegetarian = False

if vegan == 'Yes':
    vegan = True
else:
    vegan = False

if gluten_free == 'Yes':
    gluten_free = True
else:
    gluten_free = False

#Spacing
print()

#Using if statements to print out the information:
if vegetarian == False and vegan == False and gluten_free == False:
    print('Here are your restaurant choices. \nJoe\'s Gourmet Burgers', end ='')
    print('\nMama\'s Fine Italian\nMain Street Pizza Company\nCorner Café', end = '')
    print('\nThe Chef\'s Kitchen')
elif vegetarian == True and vegan == False and gluten_free == False:
    print('Here are your restaurant choices. \nMama\'s Fine Italian', end = '')
    print('\nMain Street Pizza Company\nCorner Café\nThe Chef\'s Kitchen')
elif vegetarian == False and vegan == False and gluten_free == True:
    print('Here are your restaurant choices. \nMain Street Pizza Company', end = '')
    print('\nCorner Café\nThe Chef\'s Kitchen')
elif vegetarian == True and vegan == False and gluten_free == True:
    print('Here are your restaurant choices. \nMain Street Pizza Company', end = '')
    print('\nCorner Café\nThe Chef\'s Kitchen')
elif vegetarian == False and vegan == True and gluten_free == False:
    print('Here are your restaurant choices. \nCorner Café\nThe Chef\'s Kitchen')
elif vegetarian == False and vegan == True and gluten_free == True:
    print('Here are your restaurant choices. \nCorner Café\nThe Chef\'s Kitchen')
elif vegetarian == True and vegan == True and gluten_free == False:
    print('Here are your restaurant choices. \nCorner Café\nThe Chef\'s Kitchen')
elif vegetarian == True and vegan == True and gluten_free == True:
    print('Here are your restaurant choices. \nCorner Café\nThe Chef\'s Kitchen')



