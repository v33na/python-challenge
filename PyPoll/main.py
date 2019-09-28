# Modules
import os
import csv
#Set the variables
total_votes = 0
total_candidates = 0
candidates_names = []
candidate_votes = []

# Winning Candidate and Winning Count Tracker
percent = []

# Set path for file
poll_path = os.path.join("Resources", "election_data.csv")
output_path = os.path.join("Resources", "Election Analysis")
# Open and read csv
with open(poll_path, newline="") as csvfile:
     poll_reader = csv.reader(csvfile, delimiter=",")
     # Read the header row first (skip this part if there is no header)
     poll_header = next(csvfile)
     
#To loop through the data to collect the answers
     for row in poll_reader:
         total_votes = total_votes + 1
         #read in the candidate name from column 3 row 2 of csv
         candidate_in = (row[2])

         if candidate_in in candidates_names:
            candidate_index = candidates_names.index(candidate_in)
            candidate_votes[candidate_index] = candidate_votes[candidate_index] + 1
         else:
            #if candidate was not found in candidates_unique list then append to list and add 1 to vote count
            candidates_names.append(candidate_in)
            candidate_votes.append(1)
#print(f'Total votes {total_votes}')
#print(f'Each candidate: {candidates_names}')
#print(f'Index: {candidates_names.index(candidate_in)}')
#print(f"candidates votes: {candidate_votes}")

#The percentage of votes each candidate won
for x in range(len(candidates_names)):
     vote_percent = round(candidate_votes[x]/total_votes *100, 4)
     percent.append(vote_percent)     
     max_votes = max(candidate_votes)
     max_index= candidate_votes.index(max_votes)

election_winner = candidates_names[max_index] 
#print results to terminal
print("------------------------------------------------------------")
print("Election Results")
print("-------------------------------------------------------------")
print(f"The total number of votes cast : {total_votes}")
print("--------------------------------------------------------------")
for x in range(len(candidates_names)): 
    print(f"{candidates_names[x]} : {percent[x]}% ({candidate_votes[x]})")
print("------------------------------------------------------------------")
print(f"The Winner is : {election_winner}")
print("--------------------------------------------------------------")

#To export a text file with the results
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as textfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    
    #print results to Text file
    textfile.write("Election Results\n")
    textfile.write("-------------------------------------------------------------\n")
    textfile.write(f"The total number of votes cast : {total_votes}\n")
    textfile.write("--------------------------------------------------------------\n")
    for x in range(len(candidates_names)): 
        textfile.write(f"{candidates_names[x]} : {percent[x]}% ({candidate_votes[x]})\n")
    textfile.write("------------------------------------------------------------------\n")
    textfile.write(f"The Winner is : {election_winner}\n")
    textfile.write("--------------------------------------------------------------\n")
