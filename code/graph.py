import matplotlib.pyplot as plt
import os
import pandas as pd
from datetime import datetime

def getDate(dateString):
    # print(dateString)
    strpDate = dateString.replace("-", "")
    
    return datetime.strptime(strpDate, "%Y%m%d")

def main():
    # outliers = 0
    inputFolder = "combined/"

    directories = os.listdir(inputFolder)
    minDate = getDate('2020-01-01')
    
    
    
    # plt.set_yla5l("Date (after 2020)")
    
    for station in directories:
        
        path = os.path.join(inputFolder, station)
        
        df = pd.read_csv(path)
        
        df["DATE"] = pd.to_datetime(df["DATE"], format='%Y-%m-%d')
        df = df[(df['DATE'] > minDate)]
        # df = df[(df['DATE'].month == 3)]
        # df.set_index(['DATE'],inplace=True)
        ax = df.plot(x = "DATE", y = "TEMP", title = "Temperature after 2020 in Antartica Weather Station")
        ax.set_xlabel("Date (YYYY/MM/DD)")
        ax.set_ylabel("Temperature (F)")
        
        # a = input()
        
        print(df.head(10))
        
        # df.plot(x = "TEMP", y = "DATE")
                    
        # df.to_csv(path)
            
    # print(outliers)
    
    plt.show()
            
    return 0
        
if __name__ == "__main__":
    main()