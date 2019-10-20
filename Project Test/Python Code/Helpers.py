import csv
def getArray(size, fileName): 
    my_list = []
    i = 0
    with open(fileName, newline='') as f:
      reader = csv.reader(f)
      for row in reader:  
        my_list.append(int(row[0]))
        i = i + 1
        if i >= size:
            break
    return my_list

