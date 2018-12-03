#PyBank
import os
import csv

csvpath = os.path.join('..', 'PyBank','budget_data.csv')

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")   
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")
    
    for row in csvreader:

        if row[0]:
            print(f"{row[0]} is a row")

        
# Start by defining the rows of data we will operate over, from 2 to "last_row"

# "last_row - 1" should be equivalent to "total_months"

# For column 2, rows 2 to last_row, add value in cell to "total_net"

# For column 2, rows 2 to "last row-1", subtract each row from the row after it
# Sum the results
# Divide by the total months, define as "average_change"





print("Financial Analysis")
print("---------------------")
#print(f"Total Months: {total_months}")
#print(f"Total: ${total_net}")
#print(f"Average Change: ${average_change}")
#print(f"Greatest increase in profits: ${greatest_increase}")
#print(f"Greatest increase in profits: ${greatest_decrease}")