import pandas as pd

class BasicDB:
    def __init__(self, csv):
        self.mainframe = pd.read_csv(csv)
        self.mainframe.fillna('', inplace=True)

    
    def Search(self,searchTerm, criteria):
        if criteria == 'LastName':
            return self.mainframe.loc[self.mainframe['Last Name'] == searchTerm]
    
    def AddNew(self,first,last,phone,date,files):
        self.mainframe = self.mainframe.append({'First Name':first,'Last Name':last, 'Phone':phone,'Order Date':date, 'Files':files}, ignore_index=True)
        print('adding to db')