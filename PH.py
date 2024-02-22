# CS175L
# Delvis Rodriguez
# PH

hours = 2
minutes_in_hour = 60
interval_minutes = 10
readings_per_hour = int(minutes_in_hour / interval_minutes)
total_readings = readings_per_hour * hours
count = 0
total = 0
average = 0.0

for hour in range(1, hours + 1):
    count = 0
    print(f"\nHour {hour}:")
    
    for _ in range(readings_per_hour):
        count += 1

        while True:
            try:
                ph_reading = float(input(f"Reading {count} Enter PH (10-50): "))
                if 10 <= ph_reading <= 50:
                    break
                else:
                    print('ERROR - PH must be an integer from 10 thru 50. Re-Enter')
            except ValueError:
                print('ERROR - PH must be an integer from 10 thru 50. Re-Enter')

        total += ph_reading

if total > 0:
    average = total / total_readings

print(f"\nAverage PH: {average:.2f}")








                    
