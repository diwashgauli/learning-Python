import csv
with open('data.csv') as file:
    reader =csv.reader(file)
    for line in reader:
        print(line)

with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'Country'])
    writer.writerow(['Alice', 30, 'USA'])
    writer.writerow(['Bob', 25, 'Canada'])
    writer.writerows([
    ['Alice', 30],
    ['Bob', 25]
                    ])



#assignment
#writer 
#todo with this concept
