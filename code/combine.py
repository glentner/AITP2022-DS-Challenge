import matplotlib.pyplot as plt
import pandas as pd
import os

def getFileName(fileName):
    temp =  os.path.basename(fileName)
    return temp.split(".")[0] ##Return all text before the first.

def main():
    ## 1957 is when Antarctica data starts
    dataFolder = "parsed"
    stations = {}
    directories = os.listdir(dataFolder)
    
    for year in directories:
        
        basepath = os.path.join(dataFolder, year)
        csvs = os.listdir(basepath)
            
        for csv in csvs:
              
            if csv not in list(stations.keys()):
                stations[csv] = []
                
            fullPath = os.path.join(basepath, csv)
                
            data = pd.read_csv(fullPath)
            stations[csv].append(data)
            
            
    for key in list(stations.keys()):
        df = pd.concat(stations[key], ignore_index=True)
        
        df.to_csv("combined/{}".format(key))

if __name__ == "__main__":
    main()