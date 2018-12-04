#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

## PyPoll
import os
import csv
import datetime
from datetime import date
today = str(date.today())

csvpath = os.path.join('..', 'PyPoll','election_data.csv')

# Determine total votes
total_votes = int(0)
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")   
    csv_header = next(csvreader)

    for row in csvreader:
        if row[0]:
            total_votes += 1

#Get a complete list of candidates who received votes
last_name = []
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")   
    csv_header = next(csvreader)

    for row in csvreader:
        if row[2] not in last_name:
            last_name.append(str(row[2]))




percent_won = []
total_won = []

candidate = [] #list of candidates for dictionary

print(f"                                   ")
print(f"                                   ")
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes}")
print(f"------------------------")

#For n in range(len(last_name))
#    candidate[n] = {"name":str(last_name[n]), "percent":percent_won[n], "total":total_won[n]}
#    print(f"{(candidate[n]["name"])}: {(candidate[n]["percent"])} ({(candidate[n]["total"])})")

#print(f"-------------------------")
#print(f"Winner: {winner}")
#print(f"-------------------------")
