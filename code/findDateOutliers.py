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

    directories = os.listdir(input)
    
    for station in directories:
        
        path = os.path.join(input, station)
        
        df = pd.read_csv(path)
        
        dates = df["DATE"]
        
        oldDate = getDate(dates[0])
        
        for i in dates[1:-1].index:
            if(isOutlier(dates[i], dates[i - 1], dates[i + 1])):
                print(dates[i], dates[i - 1], dates[i + 1])
                outliers += 1
                df = df.drop(i)
                
        df.to_csv(path)
            # oldDate = getDate(date)'
            
    print(outliers)
            
    return 0
        
if __name__ == "__main__":
    main()