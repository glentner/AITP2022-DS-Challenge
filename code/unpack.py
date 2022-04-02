import os
import tarfile
import pandas as pd
import io
import multiprocessing as mp

stationList = [
    "89027099999",
    "89510099999",
    "89512099999",
    "89514099999",
    "89524099999",
    "89528099999"
]

def getFileName(fileName):
    temp =  os.path.basename(fileName)
    
    return temp.split(".")[0] ##Return all text before the first .

def parseFile(queue, path, year):
    tar = tarfile.open(path, 'r:gz')
    csv_files = [f.name for f in tar.getmembers() if f.name.endswith('.csv')]
    # csv_file = csv_files[0] # here we read first csv file only
    for csv_file in csv_files:

        if csv_file[:-4] in stationList:
    
            csv_contents = tar.extractfile(csv_file).read()
            df = pd.read_csv(io.BytesIO(csv_contents), encoding='utf8', nrows = 1)
            
            # print((df["NAME"][0]).split(","))
            
            nameSplit = str(df["NAME"][0]).split(",")
            
            if len(nameSplit) > 1:
                print(nameSplit)
                
                if "AY" == nameSplit[1]:
                    print(df)
                    tar.extract(csv_file, path="parsed/{}".format(year))
            
    queue.put("{} Fully complete".format(path))

def main():
    ## 1957 is when Antarctica data starts
    inputFolder = "data/"
    outputFolder = "parsed/"
    # print(os.listdir(inputFolder))
    
    q = mp.Queue()
    processes = []

    for path in os.listdir(inputFolder):
        fullPath = os.path.join(inputFolder, path)
        
        year = getFileName(fullPath)
        
        if int(year) > 1957:
            print("Parsing year: {}".format(year))
            
            p = mp.Process(target=parseFile, args=(q, fullPath, year))
            p.start()
            processes.append(p)
            
    for process in processes:
        print(q.get())
        p.join()
            

##Test only using the latest dataset to save time
def test():
    
    inputFolder = "data/"
    outputFolder = "parsed/"
    
    testfile = "data/2022.tar.gz"
    
    tar = tarfile.open(testfile, 'r:gz')
    csv_files = [f.name for f in tar.getmembers() if f.name.endswith('.csv')]
    # csv_file = csv_files[0] # here we read first csv file only
    for csv_file in csv_files:
        csv_contents = tar.extractfile(csv_file).read()
        df = pd.read_csv(io.BytesIO(csv_contents), encoding='utf8', nrows = 1)


if __name__ == "__main__":
    main()