import os
import csv

# Set Path to collect data
election_data=os.path.join("Resources","election_data.csv")

with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
# Skips first row    
    csv_header = next(csvreader)
#Set lists and Variables
    total_vote_count=0
    candidates=[]
    votes=[]
    percent_votes=[]
    winner=0
#Analyzes data per instructions
    for row in csvreader:
      #Calculates number of total votes  
        total_vote_count+=1
      #Add unique candidate values to a list, adds candidate vote count to a seperate list  
        if row[2] not in candidates:
            candidates.append(row[2])
            index_1=candidates.index(row[2])
            votes.append(1)
        else:
            index_1=candidates.index(row[2])
            votes[index_1] += 1
#Calculate vote percentage   
    for vote in votes:
        percentage = (vote/total_vote_count) * 100
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
#Declares a winning candidate
    winner=max(votes)
    index_2=votes.index(winner)
    final_winner=candidates[index_2]
 
    
#Print Statements
    #Write to text file
    text_path=os.path.join("Analysis","Analysis.txt")
    with open(text_path,"w") as f:
        print("'''text",file=f)
        print("-------------------------",file=f)
        print(f'Total Votes: {total_vote_count}',file=f)
        print("-------------------------",file=f)
        for i in range(len(candidates)):
            print(f"{candidates[i]}: {str(percent_votes[i])} ({str(votes[i])})",file=f)
        print("-------------------------",file=f)
        print(f'Winner: {final_winner}',file=f)
        print("-------------------------",file=f)
    
    
    #Terminal Output
    print("'''text")
    print("-------------------------")
    print(f'Total Votes: {total_vote_count}')
    print("-------------------------")
    for i in range(len(candidates)):
        print(f"{candidates[i]}: {str(percent_votes[i])} ({str(votes[i])})")
    print("-------------------------")
    print(f'Winner: {final_winner}')
    print("-------------------------")