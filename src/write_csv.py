import sys
import csv
import re
import os
from msds510 import util

def updateHeader(inputFileHeader):
    fieldnames = []
    for header in inputFileHeader:
        new_header = pythonFiendlyName(header)
        fieldnames.append(new_header)
    return fieldnames


def pythonFiendlyName(name):
    nice_name = re.sub('\W+',' ',name).lower().strip().replace(' ','_')
    return nice_name


def CSVDictWriter(inputFilePath, outputFilePath):
    try:
        inputFile = open(inputFilePath, 'r')
        inputFileContent = csv.DictReader(inputFile)
        inputFileHeader = inputFileContent.fieldnames
        inputFileHeader = updateHeader(inputFileHeader)     # Updated header to Python friendly names
        outputFile = open(outputFilePath, 'w', newline='')
        outputFileContent =  csv.DictWriter(outputFile, inputFileHeader)
        outputFileContent.writeheader()
        for inputFileRow in inputFileContent:
            outputFileRow = {pythonFiendlyName(key): value for key, value in inputFileRow.items()}
            outputFileContent.writerow(outputFileRow)
        inputFile.close()
        outputFile.close()
        print('File avengers_processed.csv created and copied to {}'.format(outputFilePath))
    except BaseException  as e:
        print(str(e))
        print("Error during processing. Please try again")


if __name__ == "__main__":
    if (util.verifyArguments(sys.argv)):
        CSVDictWriter(sys.argv[1],sys.argv[2])
