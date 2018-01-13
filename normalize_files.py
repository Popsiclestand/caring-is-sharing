# !/usr/bin/env python
# title           :normalize_files.py
# description     :FIGHT BACK against poor file naming!
# author          :Popsiclestand - goldfinger59@gmail.com
# date            :20180110
# version         :3.1
# usage           :python normalize_files.py
# notes           :Use at your own risk
# python_version  :3.6
# =================================================================

# import libraries
import os
import os.path
# attempt to import from future library if present
try:
    from builtins import input
except ImportError:
    pass

primaryFilterSymbolsReplace = [' _', ' -', '_ ', '- ', ' ', '{', '}', '[', ']', ';', ':', '^', '+', '=', '<', '>', '|']
filterSymbolsDelete = ['"', "'", '*', '(', ')', '!', '?', ',', '%', '@']
secondaryFilterSymbolReplace = ['__']


# warnings and information
warningVersion = "This script runs best using Python 3.6 or higher. It is compatible with and has been tested on \
OSX and Windows systems.\n"

warningIMF = "WARNING: Do not use this on IMF packages! IMF naming convention for files and folders is \
key to the integrity of the package and should remain as delivered.\n"

infoPurpose = '''The purpose of this script is to remove spaces and special characters from folders, subfolders, and files.\n
Here are way things will change:\n
REPLACE WITH UNDERSCORE: Spaces, Brackets (square and angle), Carats, Curly Braces, Plus Signs, Colons, Semi-Colons, \n
COMPLETELY DELETED: Apostrophes, Double and Single Quotes, Exclamation Points, Question Marks, @ Symbols, Percent Signs, Stars\n
OTHER: Ampersand = n, # = Num
'''


def normalize_files_folders(directoryname):
    # check for valid path
    if os.path.isdir(directoryname):
        originalRoots = []
        originalFilesFullPath = []
        changeRoots = []
        changeFiles = []

        # navigate through a directory recursively
        for roots, dirs, files in os.walk(directoryname, topdown=False):
            # pull full path of directories and subdirectories into a list of tuples
            for dir in dirs:
                if dir[0] != '.':
                    tempTup =(roots,dir)
                    originalRoots.append(tempTup)
            # pull full path of individual files into a list of tuples
            for file in files:
                if file[0] != '.':
                    tempPathString = (roots,file)
                    originalFilesFullPath.append(tempPathString)

        # rename files
        for path in originalFilesFullPath:
            tempString = path[1]
            for symbol in primaryFilterSymbolsReplace:
                if symbol in tempString:
                    tempString = tempString.replace(symbol, '_')

            for symbol in filterSymbolsDelete:
                if symbol in tempString:
                    tempString = tempString.replace(symbol, '')

            if '&' in tempString:
                tempString = tempString.replace('&', 'n')
            elif '#' in tempString:
                tempString = tempString.replace('#', 'Num_')

            for symbol in secondaryFilterSymbolReplace:
                if symbol in tempString:
                    tempString = tempString.replace(symbol, '_')

            changePath = (path[0], tempString)
            changeFiles.append(changePath)
        combineFiles = list(zip(originalFilesFullPath,changeFiles))

        # rename folders bottom up
        for tup in originalRoots:
            tempString = tup[1]
            for symbol in primaryFilterSymbolsReplace:
                if symbol in tempString:
                    tempString = tempString.replace(symbol, '_')

            for symbol in filterSymbolsDelete:
                if symbol in tempString:
                    tempString = tempString.replace(symbol, '')

            for symbol in secondaryFilterSymbolReplace:
                if symbol in tempString:
                    tempString = tempString.replace(symbol, '_')

            if '&' in tempString:
                tempString = tempString.replace('&', 'n')
            elif '#' in tempString:
                tempString = tempString.replace('#', 'Num_')

            changeTup = (tup[0],tempString)
            changeRoots.append(changeTup)
        combineRoots = list(zip(originalRoots,changeRoots))

        try:
            for tup in combineFiles:
                os.rename(os.path.join(tup[0][0], tup[0][1]), os.path.join(tup[1][0], tup[1][1]))
            for tup in combineRoots:
                os.rename(os.path.join(tup[0][0], tup[0][1]), os.path.join(tup[1][0], tup[1][1]))
        except Exception as e:
            print(e)
            pass

        print("You have just won the war against poor naming conventions. \nAll spaces and \
invalid characters have been removed from file and directory names.\nFight on, Comrade!\n")
    else:
        print("Invalid Path.")


def main():
    print("\nWelcome to the Naming Normalizer!\n")
    print(warningVersion)
    print(infoPurpose)
    print(warningIMF)
    print("As always, use at your own risk.\n")
    try:
        directoryName = input('Input Path You\'d Like To Normalize. >>')
    except:
        print("\nYou are using an outdated version of Python. Please upgrade to Python 3.5 or higher (or pip install future).")
    else:
        normalize_files_folders(directoryName)


if __name__ == '__main__':
    main()
