# CS175L
# Delvis Rodriguez
# PH

# Constants

hours = int(2)
minutes_in_hour = int(60)
interval_minutes = int(10)
reading = int(minutes_in_hour/interval_minutes)
count = int(0)
total = int(0)
average = float(0.0)

for x in range (hours):
    count += 1
    print(f'Hour: {count}')
    for y in range (0, minutes_in_hour, interval_minutes):
        time = int(1)
        inside_1 = int(input('Reading 1 enter PH (10-50) '))
        inside_2 = int(input('Reading 2 enter PH (10-50) '))
        inside_3 = int(input('Reading 3 enter PH (10-50) '))
        inside_4 = int(input('Reading 4 enter PH (10-50) '))
        inside_5 = int(input('Reading 5 enter PH (10-50) '))
        inside_6 = int(input('Reading 6 enter PH (10-50) '))
        if (inside_1 < 1) or (inside_1 > 50):
            inside_1 == false
            if (inside_2 < 1) or (inside_2 > 50):
            inside_1 == false
                if (inside_3 < 1) or (inside_3 > 50):
                inside_1 == false
                    if (inside_4 < 1) or (inside_4 > 50):
                    inside_1 == false
                        if (inside_5 < 1) or (inside_5 > 50):
                        inside_1 == false
                            if (inside_6 < 1) or (inside_6 > 50):
                            inside_1 == false
            
        
             while (inside < 10) or (inside > 50):
            print(f'ERROR - PH must be an integer from 10 thru 50. Re-Enter')
            inside = int(input('Reading 1 Enter PH (10-50) '))
        total += inside_1
        total += inside_2
        total += inside_3
        total += inside_4
        total += inside_5
        total += inside_6
        time += 1

average = reading
print(f'Average PH: {average:.2f}')

                    
