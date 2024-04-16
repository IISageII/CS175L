#CS175L
#Delvis Rodriguez
#expensePieChart

#Modules imported
import sys
import matplotlib.pyplot as plt

def main():
    try:
        file_name = open('expenses.txt', 'r')
        file_list = [row.strip().split('\t') for row in file_name]

        slice_labels = []
        expenses = []
        
        for content in file_list:
            try:
                value = int(content[1])
                slice_labels.append(content[0])
                expenses.append(value)
            except ValueError:
                print(f'Invalid value "{content[1]}" found in the file. The value must be an integer.')
            

        #Create a pie chart from the values
        plt.pie(expenses, labels=slice_labels)

        #Add a title
        plt.title('Monthly Expenses')

        #Display the pie chart
        plt.show()

    except IOError:
        sys.exit('Cannot find the file expenses.')
                            

if __name__ == '__main__':
         main()

