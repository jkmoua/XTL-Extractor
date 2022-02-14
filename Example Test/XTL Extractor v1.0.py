#   This script iterates through all .zip files in the current working directory 
#   and will check if the 'evaluation.json' file for the respective
#   .zip file has a mould value higher than a specified value. 
#   If it does, then it will then extract the respective 'EQ.xtl' file to a directory
#   called 'XTL files meeting criteria'
import zipfile
import json
import os

#   Main function creating directory for extracted files and iterating through .zip files
def main():
    if not os.path.exists(cwd + '/' + dirName):
        os.mkdir(dirName)

    #Assign files in current working directory to variable for iteration
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        if f.endswith('.zip'):
            with zipfile.ZipFile(f) as myzip:
                for filename in myzip.namelist():
                    jsonParse(filename, myzip)

    print('Finished! Files have been extracted to folder named "' + dirName + '"')
    print('You may close the program.')
    input()

#   Iterating through .zip archive searching for 'evaluation.json' files
#   Load 'evaluation.json' files and search for Mould criteria
#   Calls xtlExtract() function if mould criteria is met
def jsonParse(f, myzip):
    if str(f).endswith('evaluation.json'):
        g = myzip.open(f)
        data = json.load(g)

        for i in data['General']:
            if i == 'Mould':
                j = data['General'][i]['Score']
                if j >= int(mouldCriteria):
                    for filename in myzip.namelist():
                        xtlExtract(filename, myzip)
        
        g.close()

#Extract corresponding .xtl file in .zip directory to specified folder
def xtlExtract(f, myzip):
    if f.endswith('EQ.xtl'):
        print('Checking and Extracting XTL files...')
        myzip.extract(f, cwd + '/' + dirName)

if __name__ == '__main__':
    mouldCriteria = input('Enter mould score greater than or equal to? ')
    print('Beginning extraction of XTL files with mould score larger than ' + mouldCriteria)
    cwd = os.getcwd()
    dirName = 'Mould Greater Than ' + mouldCriteria
    main()

