import csv
a = 0
with open("E:\query.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        linkdata = open('E:\indixe.txt', 'r', encoding='latin-1')
        for data in linkdata:
            if str.find(data, row[0]) != -1:
                a = a+1
        if a != 0:
            f = open('E:/matrix.txt', 'a')
            f.write('true')
            f.write('\n')
            a = 0
            f.close()
        else:
            f = open('E:/matrix.txt', 'a')
            f.write('False')
            f.write('\n')
            a = 0
            f.close()

linkdata.close()