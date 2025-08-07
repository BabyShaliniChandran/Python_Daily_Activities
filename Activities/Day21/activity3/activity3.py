import csv

# Step 1: Write to output.csv
with open('data.csv', newline='') as infile, open('output.csv', 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writerow(outfile, quotechar='-', quoting=csv.QUOTE_MINIMAL)
    # Modify and write rows
    for row in reader:
        row[1] = f"-{row[1]}-"
        writer.writerow(row)

# Step 2: Read from output.csv
with open('output.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
