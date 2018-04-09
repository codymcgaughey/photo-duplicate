import os
import shutil

# srcPath = ""
# srcImg = ""
# dstPath = ""
dstImg = ""
# numCopies = 0

# Have user name folder. Creates folder on desktop.
dstPath = input("Name the folder where the images will be stored: ")

# Set destination path/output folder
dstPath = os.path.join('~/Desktop', dstPath)

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
print("Output folder: " + dstPath)


# Create destination folder
if not os.path.exists(dstPath):
    os.makedirs(dstPath)

os.makedirs('~/Desktop/photoduplicate')

# Copy file

if srcExt == '.png':
    for i in range(1, numCopies + 1):
        shutil.copy2(srcImg, '~/Desktop/photoduplicate/{:02}.png'.format(i))
else:
    print('Incompatible file type')

# TODO
# Use branches
# Make loop to check if default destination path exists
# Add functionality for multiple image types

