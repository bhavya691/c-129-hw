import csv
dataset1 = []
dataset2 = []

with open('bright_stars.csv', 'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset1.append(row)

with open('unit_converted_stars.csv', 'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset2.append(row)

header1 = dataset1[0]
header2 = dataset2[0]
data1 = dataset1[1:]
data2 = dataset2[1:]

headers = header1 + header2 
data = []

for index, data_row in enumerate(data1):
    data.append(data1[index] + data2[index])

with open('result.csv', 'a+') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(data)