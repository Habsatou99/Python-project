
def writeDataToCsvFile(data,file):         

    file=open('Doc4.csv','w')
    for line in data:
        for cell in line:
            file.write(cell)
            file.write("\n")