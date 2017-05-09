#! python3

'''
Goal is to find a CSV file, see some simple stats. 



'''

import csv, os

userhome = os.environ['HOME']

def finder(): 
    for folder, subfolders, files in os.walk(userhome):
        for filename in files:
            if filename.endswith('.csv'):
                url = os.path.join(folder, filename)
                print(url)
                

def handleCSV():
    filepath = input("Enter a file to browse: ")
    file = open(filepath)
    legere = csv.reader(file)
    for row in legere:
        if legere.line_num == 1:
            print(row)


def main():
    print('CSV explorer, no jokes about comma chameleons')
    finder()
    print('----------')
    handleCSV()
    

# now run it-
main()
