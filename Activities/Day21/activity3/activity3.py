import csv
rows=[
["Name","Age","City"],
["Alice",30,"New York"],
["Bob",25,"London"]
]
with open('data.csv','w',newline='') as infile:
	writer=csv.writer(infile)
	writer.writerows(rows)


with open('data.csv', newline='') as infile, open('output.csv', 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile, quotechar='-', quoting=csv.QUOTE_NONNUMERIC)
    next(reader)
    for row in reader:
        writer.writerow(row)

with open('output.csv',newline='')as f:
	reader=csv.reader(f)
	for row in reader:
		print(row)