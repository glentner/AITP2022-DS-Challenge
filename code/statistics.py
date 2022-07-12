from datetime import datetime
import os
import pandas as pd
from pyod.models.ecod import ECOD

def getDate(dateString):
    # print(dateString)
    strpDate = dateString.replace("-", "")
    
    return datetime.strptime(strpDate, "%Y%m%d")

def isOutlier(date, lastDate, nextDate):
    
    date = getDate(date)
    lastDate = getDate(lastDate)
    nextDate = getDate(nextDate)
    
    dateDiffBefore = lastDate - date
    dateDiffAfter = nextDate - date
    
    ##If it's two dates from different years then it doesn't matter
    if dateDiffBefore.days > 365 or dateDiffAfter.days > 365:
        return False
    
    ##More than 7 days of isolation it's an outlier
    elif dateDiffAfter.days > 7 or dateDiffBefore.days > 7:
        return True
    
    else:
        return False

def main():
    outliers = 0
    input = "combined/"
    
    dataframes = []
    
    directories = os.listdir(input)
    
    for station in directories:
        
        path = os.path.join(input, station)
        
        df = pd.read_csv(path)
        
        dataframes.append(df)
        
        # combinedData = pd.concat(dataframes)

        maxtempMax = df["MAX"].idxmax()
        mintempMax = df["MIN"].idxmax()
        avgtempMax = df["TEMP"].idxmax()
        
        print(maxtempMax, mintempMax, avgtempMax)
        
        print(df["MAX"][maxtempMax], df["MIN"][mintempMax], df["TEMP"][avgtempMax])
            
    print(outliers)
            
    return 0
        
if __name__ == "__main__":
    main()