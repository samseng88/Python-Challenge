import os
import csv

# Set path for file
csvpath = os.path.join('Resources', 'election_data.csv')

# Determine the variables
total_votes = 0
candidate_votes = {}
candidate_list = []
votes_count = []
percent_votes = []
winner = ""
winner_votes = 0
new_output = []

# Read csv file
with open(csvpath,"r",newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter= ",")
    csv_header = next(csvreader)

    # Skip header for count of total votes
    for row in csvreader:
        total_votes = total_votes + 1
        
        # Loop through list to get the vote count
        candidate = row[2]
        if candidate in candidate_list:
            candidate_votes[candidate] = candidate_votes[candidate] + 1

        else:
            candidate_list.append(candidate)
            candidate_votes[candidate] = 1

    # Calculate number of votes per candidate
    for elected, ballots in candidate_votes.items():
        votes_count.append(ballots)
        votes = candidate_votes[candidate]
        
        # Get the percentage of votes per candidate
        percentage_voted = round((int(ballots)/ total_votes * 100),2)
        percent_votes.append(percentage_voted)

        # Determine the winner
        if (ballots > winner_votes):
            winner_votes = ballots
            winner= elected
    
    # Zip 3 lists for output
    new_output = zip(candidate_list,percent_votes, votes_count)
    new_output = list(new_output)

    # Generate Summary
    print("Election Results")
    print("------------------------------")
    print(f'Total Votes :  {total_votes}')
    print("------------------------------")
    for item in new_output:
        print(f'{item[0]} : {item[1]}0% ({item[2]})')
    print("------------------------------")
    print(f'Winner : {winner}')
    print("------------------------------")

# Create text output file
output_file = os.path.join( "Analysis", "election_analysis.txt")
with open(output_file,"w",newline="") as datafile:
    writer = csv.writer(datafile)

# Export a text file to Analysis folder
output_file = os.path.join( "Analysis", "election_analysis.txt")
with open(output_file,"w",newline="") as datafile:
    csvwriter = csv.writer(datafile)

with open(output_file, "w") as datafile:
    datafile.write('Election Results\n')
    datafile.write('--------------------------------------\n')
    datafile.write(f'Total Votes:  {total_votes}\n')
    datafile.write('--------------------------------------\n')
    
    for item in new_output:
        datafile.write(f'{item[0]} : {item[1]}0% ({item[2]})\n')
    datafile.write('----------------------------------------\n')
    datafile.write(f'Winner: ({winner})\n')
    datafile.write('----------------------------------------\n')