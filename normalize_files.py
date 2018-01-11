# !/usr/bin/env python
# title           :normalize_files.py
# description     :FIGHT BACK against poor file naming!
# author          :tfm
# date            :20180110
# version         :3.1
# usage           :python normalize_files.py
# notes           :Use at your own risk
# python_version  :3.6
# =================================================================


import os
import os.path
try:
    from builtins import input
except ImportError:
    pass

warningVersion = "This script runs best using Python 3.5 or higher. It is compatible with and has been tested on \
OSX and Windows systems.\n"

warningIMF = "WARNING: Do not use this on IMF packages! IMF naming convention for files and folders is \
key to the integrity of the package and should remain as delivered.\n"

warningPurpose = '''The purpose of this script is to remove spaces and special characters from folders, subfolders, and files.\n
Here are way things will change:\n
REPLACE WITH UNDERSCORE: Spaces, Brackets (square and angle), Carats, Curly Braces, Plus Signs, Colons, Semi-Colons, Back and Forward Slashes\n
COMPLETELY DELETED: Apostrophes, Double and Single Quotes, Exclamation Points, Question Marks, @ Symbols, Percent Signs, Stars\n
OTHER: Ampersand = n, # = Num
'''

def normalize_files_folders(directoryname):
    if os.path.isdir(directoryname):
        # navigate through a directory recursively
        for roots, dirs, files in os.walk(directoryname):
            if roots[0] != '.':
                newRoot = roots.replace('  ','_').replace(' _','_').replace(' -','-').replace('- ','-').replace(' ', '_').replace('&','n')\
                    .replace('#','Num').replace('*','').replace('(','').replace(')','').replace('!','').replace('?','').replace("'","").replace(',', '')\
                .replace('%','').replace('@','').replace('\\','_').replace('/','_').replace('"','').replace('{','_').replace('}','_').replace('[','_')\
                .replace(']','_').replace(';','_').replace(':','_').replace('^','_').replace('+','_').replace('<','_').replace('>','_').replace('|','_').replace('?','')
                os.rename(roots, newRoot)
        for roots, dirs, files in os.walk(directoryname):
            for singleFile in files:
                if singleFile[0] != '.':
                    replaceFileName = singleFile.replace('  ','_').replace(' _','_').replace(' -','-').replace('- ','-').replace(' ', '_').replace('&','n')\
                    .replace('#','Num').replace('*','').replace('(','').replace(')','').replace('!','').replace('?','').replace("'","").replace(',', '') \
                    .replace('%', '').replace('@', '').replace('\\', '_').replace('/', '_').replace('"','').replace('{','').replace('}','').replace('[','')\
                    .replace(']','').replace(';','').replace(':','').replace('^','').replace('+','').replace('<','_').replace('>','_').replace('|','_').replace('?','')
                    os.rename(os.path.join(roots,singleFile), os.path.join(roots,replaceFileName))
        print("You have just won the war against poor naming conventions. \nAll spaces and \
invalid characters have been removed from file and directory names.\nFight on, Comrade!\n")
    else:
        print("Invalid Path.")


print("\nWelcome to the Naming Normalizer!\n")
print(warningVersion)
print(warningPurpose)
print(warningIMF)
print("As always, use at your own risk.\n")
try:
    directoryName = input('Input Path You\'d Like To Normalize. >>')
except:
    print("\nYou are using an outdated version of Python. Please upgrade to Python 3.5 or higher.")
else:
    normalize_files_folders(directoryName)
