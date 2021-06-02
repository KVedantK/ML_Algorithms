'''
Script By:- Vedant Kulkarni
'''

import csv

class FindS_Algorithm:
    # Takes a file path input makes it to Find S hypothesis Requires Last Column to be decisive.
    def Get_Hypothesis(self,file):
        try:
            with open(file) as f:
                reader = csv.reader(f)
                data = list(reader)

            hypo = ['0']*(len(data[0])-1)
            positive_instances = []
            for i in data:
                if i[len(i)-1].lower() == 'yes':
                    positive_instances.append(i)
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

            
    #Takes Hypothesis and Query as input tells Wheather Query is Positive Example Or Negative.
    #hypo variable can be passed as instance of Get_Hypo Function Make Sure Query and Sample Hypo Attribs matches.
    def Get_Decision(self,hypo, query):
        try:
            flag = True
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


                
            


