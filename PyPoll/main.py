
#Script to analyse PyPoll data. Concept of set has been used.
# Import modules os and csv
import os

import csv

#Define and initialize variable to count total votes

total_votes = 0

#Define lists to store data

candidate_list = []

names_of_candidates = []

vote_count = []

vote_percent = []


# Define the path of input file in an object

csvpath = os.path.join("Resources","election_data.csv")

# Open and read the input file by skipping the header

with open(csvpath, newline="") as file:

    csvreader = csv.reader(file, delimiter=",")

    next(csvreader)

    #looping through the file

    for row in csvreader:

        # Count the total number of votes

        total_votes += 1
        
        # Stoing the names of candidate in candidate_list

        candidate_list.append(row[2])

    #Loop through the list of candidates and remove any duplicates using set data strucuture 

    for i in set(candidate_list):

        #Store names of unique candidate 

         names_of_candidates.append(i)
    
        # Count the total number of votes per candidate from the list

         votes_per_candidate = candidate_list.count(i)

        # The values of total vote count per candidate is stored in vote_count

         vote_count.append(votes_per_candidate)
    
        # Calculate the percent of total votes per candidate

         percent = (votes_per_candidate/total_votes)*100

         vote_percent.append(percent)

    #Find the highest count of vote from the set  

    highest_vote = max(vote_count)

    #Identify the name of the candidate with highest vote count based on same index used in the two sets
    
    winner = names_of_candidates[vote_count.index(highest_vote)]

#Storing the result of analysis in variables and printing the text to the terminal
    
Result_of_analysis = (
f"-------------------------\n"
f"Election Results\n"   
f"-------------------------\n"
f"Total Votes : {(total_votes)}\n"    
f"-------------------------\n")

print(Result_of_analysis)

for x in range(len(names_of_candidates)):
             print(f"{names_of_candidates[x]}: {round(vote_percent[x],2)}00% ({str(vote_count[x])})")

Winner =(f"-------------------------\n"
f"Winner: {winner}\n"
f"-------------------------\n"
)
print(Winner)

# Exporting the result of analysis to a text file

with open('pypoll_analysis_result.txt', 'w') as text:

     text.write(Result_of_analysis)
     for x in range(len(set(names_of_candidates))):
         text.write(names_of_candidates[x] + ": " + str(round(vote_percent[x])) +".000% (" + str(vote_count[x]) + ")\n")
     text.write(Winner)

