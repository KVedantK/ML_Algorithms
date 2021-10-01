import csv
#Converts CSV to List
def Make_Even(file):
    with open(file) as f:
        reader = csv.reader(f)
        data = list(reader)
    for i in range(0,len(data)):
        for j in range(0,len(data[0])):
            data[i][j] = data[i][j].lower()
    return data
# Calculates the number of Positive and Negative Instances return (Yes, no)
def Calculator(data):
    Yes = 0
    No = 0
    for i in data:
        if i[len(i) - 1].lower() == 'yes':
            Yes += 1
        else:
            No += 1
    return Yes,No

# Calculates the yes and no values of each instance. return {attrib:[yes, no]}
def data_Sorter(data):
    Sorted_data = {}
    for i in range(0, len(data)):
        for j in range(0,len(data[0])-1):
            if data[i][j].lower() in Sorted_data.keys():
                if data[i][len(data[0])-1].lower() == 'yes':
                    Sorted_data[data[i][j].lower()][0] += 1
                else:
                    Sorted_data[data[i][j].lower()][1] += 1
            else:
                if data[i][len(data[0])-1].lower() == 'yes':
                    Sorted_data[data[i][j].lower()] = [1,0]
                else:
                    Sorted_data[data[i][j].lower()] = [0,1]
    return Sorted_data

print(Calculator(Make_Even('findSdata.csv')))

print(data_Sorter(Make_Even('findSdata.csv')))