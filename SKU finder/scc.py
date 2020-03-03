import csv

with open("shuzhe2.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        a = 0
        cartdata = open('cart2.txt', 'r')
        for data in cartdata:
            result = str.find(data, row[0]) != -1
            data = data.strip('\n')
            data = repr(data)
            bac = repr(row[0])
            if str.find(data, bac) != -1:
                a = a+1
                break
        if a == 0:
            f = open('E:/matrix.txt', 'a')
            f.write('FALSE')
            f.write('\n')
            f.close()
        else:
            f = open('E:/matrix.txt', 'a')
            f.write('TRUE')
            f.write('\n')
            a = 0
            f.close()

cartdata.close()
