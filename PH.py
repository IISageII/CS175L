#CS175L
#Delvis Rodriguez
#PH

hours = 2
minutes_in_hour = 60
interval_minutes = 10
readings = int(minutes_in_hour/interval_minutes)
count = 0
total = 0
average = 0.0
time = 1

for x in range (1, hours + 1):
    reading_num = 0
    print(f'Hour: {time}')
    time += 1
    for y in range (readings):
        reading_num += 1
        reading_ph = int(input(f'Reading {reading_num} Enter PH (10-50) '))
        while (reading_ph < 10) or (reading_ph > 50):
            print(f'ERROR - PH must be an integer from 10 thru 50. Re-Enter')
            reading_ph = int(input(f'Reading {reading_num} Enter PH (10-50) '))
        total += reading_ph
        count += 1
    print()

Average = float(total / count)
print(f'Average PH: {Average:.2f}')
    







                    
