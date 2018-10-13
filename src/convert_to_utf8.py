import sys
import os
from msds510 import util


def convertToUTF8(inputFilePath, outputFilePath):
    try:
        sourceFile = open(inputFilePath, 'rb')
        sourceFileContent = sourceFile.read()
        sourceFile.close()
        targetFileContent = sourceFileContent.decode('ISO-8859-1')
        targetFile = open(outputFilePath, "wb")
        targetFile.write(targetFileContent.encode('utf-8'))
        targetFile.close()
        print('File avengers_utf8.csv created with utf-8 encoded data')
        print("avengers_utf8.csv copied to {}".format(outputFilePath))
    except BaseException  as e:
        print(str(e))
        print("Error during convertion. Please try again")


if __name__ == "__main__":
    if (util.verifyArguments(sys.argv)):
        convertToUTF8(sys.argv[1], sys.argv[2])
