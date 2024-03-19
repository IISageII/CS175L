#CS175L
#Delvis Rodriguez
#AverageFromInput

def main():
    data = open('numbers.txt', 'r')
    num = 0
    total = 0
    for line in data:
        num +=1
        content = float(line)
        total += float(content)
        print(f'I read in {num} number(s) Current number is:', end='')
        if content >= 0:
            print(f'    {content:.2f} Total is:    {total:.2f}')
        else:
            print(f'   {content:.2f} Total is:   {total:.2f}')
    average = float(total / num)
    print(f'Average: {average:.1f}')

if __name__ == '__main__':
    main()
    
