import os
import csv

# Set Path to collect data
csvpath=os.path.join("Resources","election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
# Skips first row
    csv_header = next(csvreader)
    total_vote_count=0
    #candidates=[]
    candidate_a=0
    candidate_b=0
    candidate_c=0
    candidate_a_votes=0
    candidate_b_votes=0
    candidate_c_votes=0
    candidate_a_percent=0
    candidate_b_percent=0
    candidate_c_percent=0
    winner=0

    for row in csvfile:
        columns=row.split(",")
        total_vote_count+=1
        value=columns[2]
    #Started trying to figure out list of variables 
        #if value in candidates:
           # candidates[value]=None
        #else:
           # candidates[value]=row
        #print(candidates)   
    #Converts Candidates into variables ***clunky, how to convert list into variables?***
        if candidate_a==0:
            candidate_a=value
        elif candidate_b==0 and candidate_a!=value:
            candidate_b=value
        elif candidate_c==0 and candidate_a!=value and candidate_b!=value:
            candidate_c=value
    # Counts votes for each candidate
        if value == candidate_a:
            candidate_a_votes+=1
        elif value == candidate_b:
            candidate_b_votes+=1
        elif value == candidate_c:
            candidate_c_votes+=1
    #Calculates vote percentage    
        candidate_a_percent='{:.3f}%'.format(candidate_a_votes/total_vote_count*100)
        candidate_b_percent='{:.3f}%'.format(candidate_b_votes/total_vote_count*100)
        candidate_c_percent='{:.3f}%'.format(candidate_c_votes/total_vote_count*100)
    #Declares winner
    if candidate_a_votes>candidate_b_votes and candidate_a_votes>candidate_c_votes:
        winner=candidate_a
    elif candidate_b_votes>candidate_a_votes and candidate_b_votes>candidate_c_votes:
        winner=candidate_b
    elif candidate_c_votes>candidate_a_votes and candidate_c_votes>candidate_b_votes:
        winner=candidate_c  
   
    
#Print Statements
    #Write to text file
    text_path=os.path.join("Analysis","Analysis.txt")
    with open(text_path,"w") as f:
        print("'''text",file=f)
        print("-------------------------",file=f)
        print(f'Total Votes: {total_vote_count}',file=f)
        print("-------------------------",file=f)
        print(f'{candidate_a}: {candidate_a_percent} ({candidate_a_votes})',file=f)
        print(f'{candidate_b}: {candidate_b_percent} ({candidate_b_votes})',file=f)
        print(f'{candidate_c}: {candidate_c_percent} ({candidate_c_votes})',file=f)
        print("-------------------------",file=f)
        print(f'Winner: {winner}',file=f)
        print("-------------------------",file=f)
    
    
    #Terminal Output  ***Showing up on different lines***
    print("'''text")
    print("-------------------------")
    print(f'Total Votes: {total_vote_count}')
    print("-------------------------")
    print(f'{candidate_a}: {candidate_a_percent} ({candidate_a_votes})')
    print(f'{candidate_b}: {candidate_b_percent} ({candidate_b_votes})')
    print(f'{candidate_c}: {candidate_c_percent} ({candidate_c_votes})')
    print("-------------------------")
    print(f'Winner: {winner}')
    print("-------------------------")