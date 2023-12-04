class Univariate():
    def quanQual(dataset):
        quan = []
        qual = []
        for columnName in dataset.columns:
            #print(columnName)
            if(dataset[columnName].dtypes == 'O'):
                #print('qual')
                qual.append(columnName)
            else:
                #print('quan')
                quan.append(columnName)
        return quan,qual
    
    
    def freqtable(ColumnName,dataset):
        freqtable = pd.DataFrame(columns = ["Unique_vaule","Frequency","Relative_Frequency","Cummulative_Frequency"])
        freqtable["Unique_vaule"] = dataset[ColumnName].value_counts().index
        freqtable["Frequency"] = dataset[ColumnName].value_counts().values
        freqtable["Relative_Frequency"] = freqtable["Frequency"] /103
        freqtable["Cummulative_Frequency"] = freqtable["Relative_Frequency"].cumsum()
        return freqtable
    
    
    def univariate(dataset,quan):
        descriptive = pd.DataFrame(index = ["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%",
                                        "99%","Q4:100%","IQR","1.5rule","Lesser", "Greater","Min","Max"],columns = quan)
        for ColumnName in quan:
            descriptive[ColumnName]["Mean"] = dataset[ColumnName].mean()
            descriptive[ColumnName]["Median"] = dataset[ColumnName].median()
            descriptive[ColumnName]["Mode"] = dataset[ColumnName].mode()[0]
            #descriptive[ColumnName]["Q1:25%"] = np.percentile(dataset[ColumnName],25)
            descriptive[ColumnName]["Q1:25%"] = dataset.describe()[ColumnName]["25%"]
            descriptive[ColumnName]["Q2:50%"] = dataset.describe()[ColumnName]["50%"]
            descriptive[ColumnName]["Q3:75%"] = dataset.describe()[ColumnName]["75%"]
            descriptive[ColumnName]["99%"] = np.percentile(dataset[ColumnName],99)
            descriptive[ColumnName]["Q4:100%"] = dataset.describe()[ColumnName]["max"]
            descriptive[ColumnName]["IQR"] = descriptive[ColumnName]["Q3:75%"] -  descriptive[ColumnName]["Q1:25%"] 
            descriptive[ColumnName]["1.5rule"] = 1.5 * descriptive[ColumnName]["IQR"]
            descriptive[ColumnName]["Lesser"] = descriptive[ColumnName]["Q1:25%"] - descriptive[ColumnName]["1.5rule"]
            descriptive[ColumnName]["Greater"] = descriptive[ColumnName]["Q3:75%"] + descriptive[ColumnName]["1.5rule"]
            descriptive[ColumnName]["Min"] = dataset[ColumnName].min()
            descriptive[ColumnName]["Max"] = dataset[ColumnName].max()
        return descriptive
    
    
    def outliercolumnName():

        lesser = []
        greater = []

        for ColumnName in quan:
            if(descriptive [ColumnName]["Min"] < descriptive [ColumnName]["Lesser"]):
                lesser.append(ColumnName)
            if(descriptive [ColumnName]["Max"] > descriptive [ColumnName]["Greater"]):
                greater.append(ColumnName)
        return ColumnName
    
    
    def replacingoutlier():

        for ColumnName in lesser:
            dataset[ColumnName][dataset[ColumnName] < descriptive[ColumnName]["Lesser"]] = descriptive[ColumnName]["Lesser"]
        for ColumnName in greater:
            dataset[ColumnName][dataset[ColumnName] > descriptive[ColumnName]["Greater"]] = descriptive[ColumnName]["Greater"]

    
    