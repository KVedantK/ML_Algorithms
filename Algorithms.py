'''
Script By:- Vedant Kulkarni
'''

import csv
import math
from re import L
class Data_Cleaner:
    def Make_Even(self,file):
        with open(file) as f:
            reader = csv.reader(f)
            data = list(reader)
        for i in range(0,len(data)):
            for j in range(0,len(data[0])):
                data[i][j] = data[i][j].lower()
        return data

class FindS_Algorithm(Data_Cleaner):
    # Takes a file path input makes it to Find S hypothesis Requires Last Column to be decisive.
    def Get_Hypothesis(self,file):
        try:
            data = self.Make_Even(file)

            hypo = ['0']*(len(data[0])-1) # creates the hypothesismost specific
            positive_instances = []
            for i in data:
                if i[len(i)-1].lower() == 'yes':
                    positive_instances.append(i) # gets a list of positive instances
            
            # checks if attribute changes if yes makes it generalized
            for j in range(0,(len(hypo))): 
                for i in range(0,(len(positive_instances))):
                    if hypo[j].lower() != positive_instances[i][j].lower() and hypo[j] == '0':
                        hypo[j] = positive_instances[i][j].lower()
                    elif hypo[j].lower() != positive_instances[i][j].lower() and hypo[j] != '0':
                        hypo[j] = '?'
                    else:
                        pass

            return hypo
        except IOError:
            print("Make Sure the File is in CSV and same directory")
        
        except:
            print("Make Sure Last Column of CSV is decisive 'Yes' for positive and 'No' for negative")

            
    # Takes Hypothesis and Query as input tells Wheather Query is Positive Example Or Negative.
    # 'hypo' variable can be passed as instance of Get_Hypo Function Make Sure Query and Sample Hypo Attribs matches.
    def Get_Decision(self,hypo, query):
        try:
            flag = True

            # checks query and hypo and gives a decision
            for i in range(0,len(query)):
                if query[i].lower() == hypo[i].lower() or hypo[i] == '?':
                    flag = True
                else:
                    flag = False
                    break
            if flag:
                return True
            else:
                return False
        
        except:
            if len(hypo) != len(query):
                print("Hypothesis and query are not for same set of instances.")
            
            else:
                print("Please Check if hypothesis is in standard form {'0' for spicific and '?' for general}")

class Decision_Tree(Data_Cleaner):
    def Entropy(self,p,n):
        if p == 0:
            x = 0
        else:
            x = -(p/(p+n))*math.log((p/(p+n)),2)
        
        if n == 0:
            y = 0
        else:
            y = (n/(p+n))*math.log((n/(p+n)),2)

        if x-y == 0:
            return 0
        else:
            return (x-y)
            
    #returns the attribute column with highest gain starting from 0 as 1st attrib in csv
    def Attrib_Entropy(self, data):
        list_attribs = list()
        list_labels = list()
        for i in range(0,(len(data[0])-1)):
            attrib_values = {}
            labels = []
            for j in range(0,len(data)):
                if data[j][i] in attrib_values.keys():
                    if data[j][(len(data[j])-1)].lower() == 'yes':
                        attrib_values[data[j][i]][0] += 1 
                    else:
                        attrib_values[data[j][i]][1] += 1 
                else:
                    labels.append(data[j][i])
                    if data[j][(len(data[j])-1)].lower() == 'yes':
                        attrib_values[data[j][i]] = [1,0] 
                    else:
                        attrib_values[data[j][i]] = [0,1] 
            
            list_attribs.append(attrib_values)
            list_labels.append(labels)
        Gains = [] #contains List Of Entropies of each element atttribute wise.
        for i in range(0,len(list_attribs)):
            sum = 0
            for j in list_labels[i]:
                pos_neg = list_attribs[i][j][0]+list_attribs[i][j][1]
                total = len(data)
                Entropy = self.Entropy(list_attribs[i][j][0],list_attribs[i][j][1])
                sum = sum + (((pos_neg/total))*Entropy)
            Gains.append((H_Dataset-sum))
        return Gains.index(max(Gains))

    def Get_Tree(self,file):
        data = self.Make_Even(file)
        positive_instances = []
        negative_instances = []
        for i in data:
            if i[len(i)-1].lower() == 'yes':
                positive_instances.append(i) # gets a list of positive instances
            if i[len(i)-1].lower() == 'no':
                negative_instances.append(i) # gets a list of positive instances
            else:
                pass
        # Gets Entropy of the dataset
        global H_Dataset 
        H_Dataset = self.Entropy(len(positive_instances), len(negative_instances))
        print(self.Attrib_Entropy(data))
Dt = Decision_Tree()
Dt.Get_Tree('findSdata.csv')
        


        