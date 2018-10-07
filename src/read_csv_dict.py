import sys
import csv

def verifyArguments():
    try:
        argumentsCount = len(sys.argv)
        if argumentsCount == 2:  # To verify number of command line arguments
                inputFileName = sys.argv[1].split("/")[-1]
                if inputFileName:  # To verify file name is not empty
                    return True
                else:
                    print("Invalid File Names")
                    return False
        else:
            print("Invalid Number of Arguments")
            return False
    except:
        return False


def CSVDictReader(inputCSVFile):
    allRows = []
    try:
        with open(inputCSVFile,'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            allRows = [row for row in csv_reader]
        print('Printing 161 Row:')
        print(allRows[160])
    except:
        print("Error during convertion. Please try again")


if __name__ == "__main__":
    if (verifyArguments()):
        CSVDictReader(sys.argv[1])
