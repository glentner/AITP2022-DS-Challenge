from datetime import datetime
import os
import pandas as pd
from pyod.models.ecod import ECOD

checkedValues = [
    "TEMP",
    "MIN",
    "MAX"
]

def main():
    outliers = 0
    input = "combined/"

    directories = os.listdir(input)
    
    for station in directories:
        
        path = os.path.join(input, station)
        
        df = pd.read_csv(path)
        
        for key in checkedValues:
        
            q1 = df[key].quantile(.25)
            q3 = df[key].quantile(.75)
            
            iqr = (q1 * q3)
            
            lowBound = q1 - 1.5 * iqr
            highBound = q3 + 1.5 * iqr
            
            for i in df[key].index:
                if df[key][i] < lowBound or df[key][i] > highBound:
                    outliers += 1
                    # print(df[key][i])
                    df = df.drop(i)
                    
                    
        df.to_csv(path)
            
    print(outliers)
            
    return 0
        
if __name__ == "__main__":
    main()