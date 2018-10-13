import datetime
import os
from datetime import date


def get_month(introValue):
    try:
        date_time_obj = datetime.datetime.strptime(introValue, '%b-%y')
    except:
        date_time_obj = datetime.datetime.strptime(introValue, '%d-%b')
    return date_time_obj.month


def get_date_joined(yearValue, introValue):
    try:
        date_time_str = yearValue + str(get_month(introValue)) + '01'
        date_time_obj = datetime.datetime.strptime(date_time_str, "%Y%m%d").date()
    except:
        print("Unable to join the date")
        return None
    return date_time_obj


def days_since_joined(yearValue, introValue):
    try:
        recordDate = get_date_joined(yearValue, introValue)
        currentDate = date.today()
        totalDays = (currentDate - recordDate).days
    except:
        print("Unable to count total number of days")
        return None
    return totalDays


def getFileNameAndPath(filePath):  # To split folder path and file name from argument
    try:
        index = filePath.rindex("/")
        inputFolderPath = filePath[0:index]
        inputFileName = filePath[index:]
        return inputFileName,inputFolderPath
    except BaseException as e:
        print("Exception in getFileNameAndPath function")
        print(str(e))


def verifyArguments(argv):
    try:
        argumentsCount = len(argv)
        if argumentsCount == 3:  # To verify number of command line arguments
            if argv[1] == argv[2]:  # To verify source and target file paths
                print("Input and output files are same. Please check file name(s) and Path")
                return False
            else:
                inputFileName, inputFolderPath = getFileNameAndPath(argv[1])
                outputFileName, outputFolderPath = getFileNameAndPath(argv[2])
                if inputFileName and outputFileName:  # To verify file names are not empty
                    if not os.path.exists(outputFolderPath):
                        print("Creating directory")
                        os.mkdir(outputFolderPath)      # Create output directory if not exist
                    return True
                else:
                    print("Invalid File Names")
                    return False
        else:
            print("Invalid Number of Arguments")
            return False
    except BaseException  as e:
        print("Exception in verifyArguments function")
        print(str(e))
        return False
