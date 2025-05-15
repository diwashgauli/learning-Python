import csv
with open('data.csv') as file:
    reader =csv.reader(file) #read in list format
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
data=[['charlie',18,'KTM'],['BOB',20,'BKT']]

with open('output.csv','w',newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

#we were reading and writing on files in list format we can do it on a dictionary format as well.


#read and write in dictionary format.
with open ('data.csv') as file:
     reader=csv.DictReader(file) #read in dictionary format: Reads data from .csv file and display it in a dictionary format.
     for row in reader:
          print(row)




data=[
     {'Name':'Max','Age':12},
     {'Name':'Payne','Age':15}

]

with open ('dictop.csv','w',newline='') as file:
     writer=csv.DictWriter(file,fieldnames=['Name','Age']) #write data that is in dictionary format .csv file ccontains data in csv format.
     writer.writeheader()
     writer.writerows(data)







#assignment
#writer 
#todo with this concept
