
def main():
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
        df = pd.concat(stations[key])
        
        df.to_csv("combined/{}".format(key))