import sys

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
    except:
        print("Error during convertion. Please try again")


if __name__ == "__main__":
    if (verifyArguments()):
        convertToUTF8(sys.argv[1], sys.argv[2])
