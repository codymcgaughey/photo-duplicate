import os
import shutil
import subprocess
import platform

#CMCG
########################
# Initializations

EXTENSIONS = ['jpg', 'jpeg', 'png']
OSPATH = os.path.abspath('~/Desktop/photoduplicate')
#dstImg = ""

########################
# Functions

# open folder after process is ran
def open_file(OSPATH):
    if platform.system() == "Windows":
        os.startfile(OSPATH)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", OSPATH])
    else:
        subprocess.Popen(["xdg-open", OSPATH])

########################
# User Input

# Have user name folder. Creates folder on desktop.
#dstPath = input("Name the folder where the images will be stored: ")

# Set destination path/output folder
#dstPath = os.path.join('~/Desktop', dstPath)

# Have user select amount of copies
numCopies = int(input("How many image files do you need? "))

# User input, set to absolute path name
isPath = 0

while isPath == 0:
    srcImg = input("Enter the path of the image file you want to copy: ")
    srcPath = os.path.abspath(srcImg)
    if os.path.exists(srcPath) == False:
        print("Path doesn't exist.")
        isPath = 0
    else:
        isPath = 1

# Gets file type
srcExt = os.path.splitext(srcImg)[1]

# Testing Output
print("Input source: " + srcPath)
print("Input image: " + srcImg)
# print("Output folder: " + dstPath)

# Create destination folder based on user input
#if not os.path.exists(dstPath):
    #os.makedirs(dstPath)

# Create default destination folder
os.makedirs('~/Desktop/photoduplicate')

# Copy files
if srcExt == '.png':
    for i in range(1, numCopies + 1):
        shutil.copy2(srcImg, '~/Desktop/photoduplicate/{:02}.png'.format(i))
else:
    print('Incompatible file type')

# Open folder after process is ran
open_file(OSPATH)

# TODO: check if default destination path exists
# TODO:

