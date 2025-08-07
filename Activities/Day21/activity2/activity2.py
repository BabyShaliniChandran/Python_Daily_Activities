import csv
with open("data.csv") as f:
	total=0.0
	reader=csv.reader(f)
	next(reader)
	for row in reader:
		total+=float(row[1])
print(total)