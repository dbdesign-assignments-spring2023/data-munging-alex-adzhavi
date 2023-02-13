import csv

h = open("data/clean_data.csv")

reader = csv.reader(h)
header = next(reader)

count = 1
sum = 0.0

for row in reader:
    if (count == 1):
        start = row[0] # Store the year of the first year in a decade
        sum = float(row[13]) # Store the annual mean J-D
    if (count == 3 and row[0] == "2022"): # Fixes that we don't have data after 2022
        print(start + " to " + row[0] + " -> {:.2f}".format(sum / count)) 
    if (count == 10): # When we reach the 10th year, print out
        print(start + " to " + row[0] + " -> {:.2f}".format(sum / count)) 
        count = 1 # Reset the count
    else:
        sum = sum + float(row[13]) 
        count = count + 1

h.close()
