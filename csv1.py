import csv
def writeDataListToCSV():
  with open("data_out_from_list.csv", "wt") as fOut:
    csvWriter = csv.writer(fOut, delimiter=",", quotechar ='"',quoting=csv.QUOTE_MINIMAL )
    
    csvWriter.writerow([3,"c,d", 987.6])
    csvWriter.writerow([4,"e,f", 56.6])
def writeDataDictToCSV():
  with open("data_out_from_dict.csv", "wt") as fOut:
    columnNames = ["c2", "c3", "c1"]
    csvWriter = csv.DictWriter(fOut, fieldnames = columnNames, delimiter=",", quotechar ='"',quoting=csv.QUOTE_MINIMAL )
    
    csvWriter.writeheader()
    csvWriter.writerow({"c1": 3,"c2": "c,d", "c3": 987.6})
    csvWriter.writerow({"c1": 4,"c2": "e,f", "c3": 56.6})
def main():
  #readCSVIntoDict()
  #writeDataListToCSV()
  writeDataDictToCSV()
if __name__ == "__main__":
   main()
