from doctest import testfile
from inspect import getfile
import os
import tarfile
import pandas as pd
import io

def getFileName(fileName):
    temp =  os.path.basename(fileName)
    
    return temp.split(".")[0] ##Return all text before the first .


def main():
    ## 1973 data is most complete
    inputFolder = "data/"
    outputFolder = "parsed/"
    print(os.listdir(inputFolder))

    # for path in os.listdir(inputFolder):
    #     fullPath = os.path.join(inputFolder, path)
        
    #     year = getFileName(fullPath)
        
    #     if int(year) > 1973:
    #         tar = tarfile.open(fullPath)
    #         print(tar.getnames())


##Test only using the latest dataset to save time
def test():
    
    inputFolder = "data/"
    outputFolder = "parsed/"
    
    testfile = "data/2022.tar.gz"
    
    tar = tarfile.open(testfile, 'r:gz')
    csv_files = [f.name for f in tar.getmembers() if f.name.endswith('.csv')]
    csv_file = csv_files[0] # here we read first csv file only
    csv_contents = tar.extractfile(csv_file).read()
    df = pd.read_csv(io.BytesIO(csv_contents), encoding='utf8')


if __name__ == "__main__":
    test()