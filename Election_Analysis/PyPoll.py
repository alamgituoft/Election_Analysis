# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv") 
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}

#Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read and print the header row.
    headers = next(file_reader)
    
    #print each row in CSV file
    for row in file_reader:
        #Add total vote count
        total_votes += 1

        #Print candidate name for each row 
        candidate_name = row[2]

        #If candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            
            #Add to list of candidates
            candidate_options.append(candidate_name)

            #Begin tracking candidate's vote count
            candidate_votes [candidate_name] = 0

        #Add a vote to candidate's count
        candidate_votes[candidate_name] += 1 

#save results to text file
with open(file_to_save, "w") as txt_file:

# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)


    #Find percentage of votes for each candidate by for loop through counts
    #Iterate through candidate list. 
    for candidate_name in candidate_votes:
        #Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #Calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        #4. print candidate name, vote count and percentage of votes
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        #Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)


        #find winning vote count and candidate
        #1. determine if votes are greater than winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true then set winning_counts = votes and winning_percent = 
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            #set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    winning_candidate_summary =(
        f"-----------------------\n"
        f"winner: {winning_candidate}\n"
        f"winning vote count: {winning_count:,}\n"
        f"winning percentage: {winning_percentage:.1f}%\n"
        f"-----------------------\n")
    #print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)









        

