#   This script iterates through all .zip files in the current working directory and will check if the 'evaluation.json' file for the respective
#   .zip file has a mould value higher than a specified value. If it does, then it will then extract the respective 'EQ.xtl' file to a directory
#   called 'XTL files meeting criteria'
import zipfile
import json
import os

def main():
    mouldCriteria = input('Enter mould score greater than or equal to? ')

    if not os.path.exists('e:/TrueSortLoggingScript/XTL files meeting criteria'):
        os.mkdir('XTL files meeting criteria')

    #Assign files in current working directory to variable for iteration
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        #Iterating through files searching for .zip files
        if f.endswith('.zip'):
            with zipfile.ZipFile(f) as myzip:
                for filename in myzip.namelist():
                    #Iterating through .zip archive searching for 'evaluation.json' files
                    #Load 'evaluation.json' files and search for Mould criteria
                    if filename.endswith('evaluation.json'):
                        g = myzip.open(filename)
                        data = json.load(g)

                        for i in data['General']:
                            if i == 'Mould':
                                j = data['General'][i]['Score']
                                #If mould criteria is met in .json file, extract corresponding .xtl file in .zip directory to specified folder
                                if j >= int(mouldCriteria):
                                    for filename in myzip.namelist():
                                        if filename.endswith('EQ.xtl'):
                                            myzip.extract(filename, 'E:/TrueSortLoggingScript/XTL files meeting criteria/')
                                            print('Checking and Extracting...')
                    
                        g.close()

    print('Finished! You may close the program.')
    input()

def jsonParse(f):
    if f.endswith('evluation.json'):
        g = open(f)

        data = json.load(g)

        for i in data['General']:
            if i == 'Mould':
                j = data['General'][i]['Score']
                #if j meets criteria, do something specified here
        
        g.close()

if __name__ == '__main__':
    main()

