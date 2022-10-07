class univariate():
    def quanqual(self,dataset):
        quan=[]
        qual=[]
        for colname in dataset.columns:
            if(dataset[colname].dtypes=='object'):
                qual.append(colname)
            else:
                quan.append(colname)
        return quan,qual
    
    def frequencytable(self,dataset,columnName):
        import pandas as pd
        freqtable=pd.DataFrame(columns=["unique_values","freuency","RelativeFreq","cumsum"])
        freqtable['unique_values']=dataset[columnName].value_counts().sort_index().index
        freqtable['freuency']=dataset[columnName].value_counts().sort_values().values
        freqtable['RelativeFreq']=(freqtable["freuency"]/len(freqtable)*100)
        freqtable['cumsum']=freqtable['RelativeFreq'].cumsum()
        return freqtable
    
    def univariate_measure(dataset):
        import pandas as pd
        import numpy as np
        MeasureTable=pd.DataFrame(index=["Mean","Mode","Median","25","50","75","100","IQR",
                                     "1.5IQR","Lesser","Greater","Min","Max"],columns=quan)

        for colname in quan:
            MeasureTable[colname]["Mean"]=dataset[colname].mean()
            MeasureTable[colname]["Mode"]=dataset[colname].mode()[0]
            MeasureTable[colname]["Median"]=dataset[colname].median()
            MeasureTable[colname]["25"]=np.percentile(dataset[colname],25)
            MeasureTable[colname]["50"]=np.percentile(dataset[colname],50)
            MeasureTable[colname]["75"]=np.percentile(dataset[colname],75)
            MeasureTable[colname]["100"]=np.percentile(dataset[colname],100)
             #IQR=Q3-Q1
            MeasureTable[colname]["IQR"]= MeasureTable[colname]["75"]- MeasureTable[colname]["25"]
            #MeasureTable[colname]["25"]-Q1 MeasureTable[colname]["50"]-Q2 
            #MeasureTable[colname]["75"]-Q3 MeasureTable[colname]["100"]-Q4
            #1.5IQR=1.5*IQR
            MeasureTable[colname]["1.5IQR"]= 1.5* MeasureTable[colname]["IQR"]
            #lesser=Q1-1.5IQR
            MeasureTable[colname]["Lesser"]=MeasureTable[colname]["25"]-MeasureTable[colname]["1.5IQR"]
            #Greater=Q3+1.5IQR
            MeasureTable[colname]["Greater"]= MeasureTable[colname]["75"]+ MeasureTable[colname]["1.5IQR"]
            MeasureTable[colname]["Min"]=MeasureTable[colname].min()
            MeasureTable[colname]["Max"]=MeasureTable[colname].max()
        return MeasureTable