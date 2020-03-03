import csv

DD=None
DD1=None
with open("shuzhe2.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        a = 0
        cartdata = open('cart2.txt', 'r')
        for data in cartdata:
            date = data.strip()
            bac = str(row[0])
            DD= date
            DD1=bac
            # if '643824322783' in bac and '643824322783' in date:
            #     print(date, repr(date), bac, repr(bac))
            if (str.find(date,bac) != -1 or str.find(bac, date) != -1) and date != '' and bac != '':
                a = a+1
                # print(date, bac)
                # f = open('matrix.txt', 'a')
                # f.write('%s, %s' % (date, bac))
                # f.write('\n')
                # f.close()
                break
        if a == 0 and date!='SKU编码':
            f = open('matrix.txt', 'a')
            f.write('FALSE,%s,%s'%(DD,DD1))
            f.write('\n')
            f.close()
        else:
            pass
            # f = open('matrix.txt', 'a')
            # # f.write('TRUE')
            # f.write('\n')
            # a = 0
            # f.close()
cartdata.close()
