# FIGHT BACK against poor file naming conventions!
# v.3 - Finally it's recursive! And also much cleaner code. Also cleans up invalid characters

import os
import os.path

warningVersion = "This script runs best using Python 3.5 or higher. It is compatible with and has been tested on\
OSX and Windows systems.\n"

warningIMF = "WARNING: Do not use this on IMF packages! IMF naming convention for files and folders is \
key to the integrity of the package and should remain as delivered.\n"

warningPurpose = "The purpose of this script is to remove spaces and special characters from folders, subfolders, \
and files from a file path you specify.\nIt replaces spaces with underscore, ampersands with lower-case \
n, # with the word Num and completely removes asterisks, exclamation points, and parenthesis.\n"


def normalize_files_folders(directoryname):
    if os.path.isdir(directoryname):
        # navigate through a directory recursively
        for roots, dirs, files in os.walk(directoryname):
            if roots[0] != '.':
                newRoot = roots.replace('  ','_').replace(' _','_').replace(' -','-').replace('- ','-').replace(' ', '_').replace('&','n')\
                    .replace('#','Num').replace('*','').replace('(','').replace(')','').replace('!','').replace('?','')
                os.rename(roots, newRoot)
        for roots, dirs, files in os.walk(directoryname):
            for singleFile in files:
                if singleFile[0] != '.':
                    replaceFileName = singleFile.replace('  ','_').replace(' _','_').replace(' -','-').replace('- ','-').replace(' ', '_').replace('&','n')\
                    .replace('#','Num').replace('*','').replace('(','').replace(')','').replace('!','').replace('?','')
                    os.rename(os.path.join(roots,singleFile), os.path.join(roots,replaceFileName))
        print ("You have just won the war against poor naming conventions. \nAll spaces and \
invalid characters have been removed from file and directory names.\nFight on, Comrade!\n")
    else:
        print("Invalid Path.")


print(warningVersion)
print(warningPurpose)
print(warningIMF)

directoryName = input('Input Path You\'d like to normalize. >>')
normalize_files_folders(directoryName)