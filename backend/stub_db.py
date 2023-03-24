import pandas as pd

class StubDB:
    def __init__(self):
        self.mainframe = self.DummyData()

    def DummyData(self) -> pd.DataFrame:
        test_data = {'First Name':['Bob', 'Joe', 'Tim', 'Meg', 'Tony'],
                     'Last Name': ['Smith', 'Kidd', 'Stumpf', 'Smith', 'Duhan'],
                     'Phone': ['6', '3','5','1','2'],
                     'Order Date':[0,0,0,0,0],
                     'Files': [0,0,0,0,0]}
        frame = pd.DataFrame(test_data)
        return frame
    
    def Search(self,searchTerm, criteria):
        if criteria == 'LastName':
            return self.mainframe.loc[self.mainframe['Last Name'] == searchTerm]