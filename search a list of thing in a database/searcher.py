import string
import csv
import codecs

cartdata = open('cart2.txt', 'r')
a = 0
with open("shuzhe2.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        for data in cartdata:
            result = str.find(data, 'J2952') != -1
            if str.find(data, 'J2952') != -1:
                a = a+1
        f = open('E:/matrix.txt', 'a')
        f.write(str(a) + ',')
        a = 0
        f.close()

cartdata.close()