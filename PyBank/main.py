import os
import csv

# Set path for file
csvpath = os.path.join('Resources', 'budget_data.csv')

# List variables
total_months = 0
net_total = 0
dataset = []
average_change = []
greatest_increase = ["",0]
greatest_decrease = ["",0]

# Open the CSV and skip header
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

# Skip the header for count
    for row in csvreader:
    # Add the total months
        total_months += 1

# Calculate the net total Profit/Lossess
        net_total = int(net_total) + int(row[1])

#Put data into a list to calculate monthly change
        dataset.append(row)
        
        #Loop through data and get the monthly change 
        for i in range(len(dataset)-1):
            average_change = int((dataset)[i + 1][1]) - int((dataset)[i][1])

        # The greatest increase in profits (date & amount)
            if  (average_change > greatest_increase[1]):
                greatest_increase[0] = row[0]
                greatest_increase[1] = average_change

        # The greatest decrease in profits (date & amount)
            if (average_change < greatest_decrease[1]):
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = average_change
        
        #The average change in losses
            average_change = round((int((dataset)[-1][1]) - int((dataset)[0][1])) / (len(dataset)-1),2)

    # Write Output file
output_path = os.path.join( "Analysis", "budget_analysis.txt")

# Generate Summary
print('Financial Analysis')
print('---------------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${net_total}')
print(f'Average Change: ${average_change}')
print(f'Greatest Incease in Profits: {greatest_increase[0]} (${greatest_increase[1]})')
print(f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})')


# Export a text file to Analysis folder
with open(output_path, "w") as csvfile:
    writer = csv.writer(csvfile)
    csvfile.write('Financial Analysis\n')
    csvfile.write('----------------------------\n')
    csvfile.write(f'Total Months:  {total_months}\n')
    csvfile.write(f'Total:  ${net_total}\n')
    csvfile.write(f'Average Change: ${average_change}\n')
    csvfile.write(f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n')
    csvfile.write(f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n')