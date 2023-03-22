import os
import csv

# Set Path to collect data
csvpath=os.path.join("Resources","budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
# Sets counts for variables 
    # and Desi is cooler than Hugo
    row_count=0
    pnlsum=0
    open_balance=0
    close_balance=0
    row_a_value=0
    row_b_value=0
    old_value=0
    max_value=0
    min_value=0
    max_name=0
    min_name=0
# Skips first row
    csv_header = next(csvreader)
# Calculates data    
    for row in csvfile:
    #Calculates total number of months included in the dataset
        columns=row.split(",")
        value=columns[1]
        row_a_value= int(old_value) #Saves the previous row value for later calculating Max/Min 
        row_count+= 1
    #Calculates net total amount of "Profit/Losses" over the entire period
        pnlsum+= int(value)
    #Calculates changes in "Profit/Losses" over the entire period,
        if row_count==1:
            open_balance+= int(value)
        if row_count==86: #***Different way to find this #?, len()?***
            close_balance+= int(value)
    #Calculates Min/Max PnL
        row_b_value= int(value)
        change_rows=(row_b_value-row_a_value)
        old_value=int(value)
        if max_value<change_rows:
            max_value=change_rows
        if max_value==change_rows:
            max_name=columns[0]
        if min_value>change_rows:
            min_value=change_rows
        if min_value==change_rows:
            min_name=columns[0]

    #Calculates the average of Profit/Loss changes
    ave_change='{:.2f}'.format((close_balance-open_balance)/(row_count-1))   
   
#*Print Statements*
 #Print to txt file
    text_path=os.path.join("Analysis","Analysis.txt")
    with open(text_path,"w") as f:
        print("'''text",file=f)
        print("Financial Analysis",file=f)
        print("-------------------------",file=f)
        print(f'Total Months: {row_count}',file=f)
        print(f'Total: ${pnlsum}',file=f)
        print(f'Average Change: ${ave_change}',file=f) 
        print(f'Greatest Increase in Profits: {max_name} (${max_value})',file=f)
        print(f'Greatest Decrease in Profits: {min_name} (${min_value})',file=f)
        print("'''",file=f)

 #Print to Terminal 
    print("'''text")
    print("Financial Analysis")
    print("-------------------------")
    print(f'Total Months: {row_count}')
    print(f'Total: ${pnlsum}')
    print(f'Average Change: ${ave_change}')
    print(f'Greatest Increase in Profits: {max_name} (${max_value})',)
    print(f'Greatest Decrease in Profits: {min_name} (${min_value})')
    print("'''")