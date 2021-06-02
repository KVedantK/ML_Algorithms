import csv
class FindS_Algorithm:
    def Find_S(file):
        with open(file) as f:
            reader = csv.reader(f)
            data = list(reader)

        hypo = ['0']*(len(data[0])-1)
        positive_instances = []
        for i in data:
            if i[len(i)-1] == 'Yes':
                positive_instances.append(i)
        print(positive_instances)
        for j in range(0,(len(hypo))): 
            for i in range(0,(len(positive_instances))):
                if hypo[j] != positive_instances[i][j] and hypo[j] == '0':
                    hypo[j] = positive_instances[i][j]
                elif hypo[j] != positive_instances[i][j] and hypo[j] != '0':
                    hypo[j] = '?'
                else:
                    pass

        return hypo

