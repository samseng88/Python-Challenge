import os
import csv

# Set path for file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Determine variables
total_months = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9]
total_revenue = 0

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        # print(row) works
        # track totals
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Profit/Losses"])

    #track profit/losses change
    revenue_change = int(row["Profit/Losses"]) - prev_revenue
    prev_revenue = int(row["Revenue"])
    revenue_change_list = revenue_change_list + [revenue_change]
    month_of_change = month_of_change + [row["Date"]]

    # Calculate greatest increase
    if (revenue_change > greatest_increase[1]):
        greatest_increase[0] = row["Date"]
        greatest_increase[1] = revenue_change
    
    # Calculate greatest decrease
    if (revenue_change < greatest_decrease[1]):
        greatest_decrease[0] = row["Date"]
        greatest_decrease[1] = revenue_change

# Calculate the Average Revenue Change
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)

# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"---------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue Change: ${revenue_avg}\n"
    f"Greatest Incease in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the output
print(output)

#Export the results to the text file