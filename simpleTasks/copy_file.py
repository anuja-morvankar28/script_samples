
 """
    import package

    """

import sys
from shutil import copyfile
from sys import exit
import shutil

"""
    initialize variable
    take input from user
    
     """

source = input("Enter source file: ")
target = input("Enter target file: ")
try:
    shutil.copyfile(source, target)
except IOError as e:
    print("Unable to copy file. %s" % e)
    exit(1)
except:
    print("Unexpected error:", sys.exc_info())
    exit(1)
    print("\nFile copy done!\n")
while True:
    print("Do you like to print the file ? (y/n): ")
    check = input()
    if check == 'n':
        break
    elif check == 'y':
        file = open(target, "r")
        print("\nHere follows the file content:\n")
        print(file.read())
        file.close()
        print()
        break
    else:
        continue