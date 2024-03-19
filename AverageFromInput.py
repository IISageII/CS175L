#CS175L
#Delvis Rodriguez
#AverageFromInput

def main():
    import sys
    try:
        data = open('numbers.txt', 'r')
    except IOError:
        sys.exit('File not found: numbers.txt - exiting')
    num = 0
    total = 0
    for line in data:
        try:
            content = float(line)
            total += float(content)
            num +=1
            print(f'I read in {num} number(s) Current number is:', end='')
            if content >= 0:
                print(f'    {content:.2f} Total is:    {total:.2f}')
            else:
                print(f'   {content:.2f} Total is:   {total:.2f}')
        except ValueError:
            print(f'Bad data: {line.strip()} skipping')
    data.close()
    average = float(total / num)
    print(f'Average: {average:.1f}')

if __name__ == '__main__':
    main()
    
