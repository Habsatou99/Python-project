import csv
def readDataFromCsvFile(file_name):
 file_name= open(file_name)
 file_read =csv.reader(file_name)
 array = list(file_read)
 return array