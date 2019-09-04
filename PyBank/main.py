#Python script to analyze financial records of a company over a period of time

#import modules

import os

import csv

# Define variable to store list of data

list_profit_loss= []

date = []

change_in_profit_loss = []

#Loading file path to an object

csvpath = os.path.join("Resources", "budget_data.csv")

# Open and read the csv by skipping header

with open (csvpath, newline='') as csv_file:

     csv_reader = csv.reader(csv_file, delimiter=',')

     next(csv_reader)
     
     for row in csv_reader:
        
        #Storing data from the columns into two lists with type conversion of row[1] (Profit/loss) on which further analysis can be performed
        
        list_profit_loss.append(float(row[1]))

        date.append(row[0])
    
    
     total_amount = sum(list_profit_loss)
    
     total_months = len(date) 

     #Looping through the list of profit/loss to calculate the difference in consecutive values to find the change in profit/loss
     
     for i in range(1,len(list_profit_loss)):

         change_in_profit_loss.append(list_profit_loss[i] - list_profit_loss[i-1])   
         
         #computing average change in profit and loss

         average_change = sum(change_in_profit_loss)/len(change_in_profit_loss)

        #Identify greatest increase and decrease in profit/loss 

         greatest_increase_profit = max(change_in_profit_loss)

         greatest_decrease_profit = min(change_in_profit_loss)

        #Extracting the dates corresponding to the greatest increase and decrease in profit/loss 
        #+1 is used to match the index of the amount with date because the first data element in profit/loss has 
        # nothing before it to compute difference, hence the result shifts by 1 row. Better understood by writing a new csv

         max_change_date = str(date[change_in_profit_loss.index(max(change_in_profit_loss))+1])

         min_change_date = str(date[change_in_profit_loss.index(min(change_in_profit_loss))+1])

     Result_of_Analysis =(f"Financial Analysis \n" f"--------------------\n" f"Total Months: {total_months} \n"
     f"Total: ${round(total_amount)}\n"f"Avereage Change: ${round(average_change,2)}\n"f"Greatest Increase in Profits:  {max_change_date} (${round(greatest_increase_profit)})\n"
     f"Greatest Decrease in Profits:  {min_change_date} (${round(greatest_decrease_profit)})\n")

     print (Result_of_Analysis)

     # Exporting the result of analysis to a text file

     with open ("Result_of_pybank_analysis.txt", "w") as textfile:
         
        textwriter = textfile.write(Result_of_Analysis)