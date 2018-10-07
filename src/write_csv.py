import sys
import csv
import re

def verifyArguments():
    try:
        argumentsCount = len(sys.argv)
        if argumentsCount == 3:  # To verify number of command line arguments
            if sys.argv[1] == sys.argv[2]:  # To verify source and target file paths
                print("Input and output files are same. Please check file name(s) and Path")
                return False
            else:
                inputFileName = sys.argv[1].split("/")[-1]
                outputFileName = sys.argv[2].split("/")[-1]
                if inputFileName and outputFileName:  # To verify file names are not empty
                    return True
                else:
                    print("Invalid File Names")
                    return False
        else:
            print("Invalid Number of Arguments")
            return False
    except:
        print("Exception in verifyArguments function")
        return False


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
    except:
        print("Error during processing. Please try again")


if __name__ == "__main__":
    if (verifyArguments()):
        CSVDictWriter(sys.argv[1],sys.argv[2])
