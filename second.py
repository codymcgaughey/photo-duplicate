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
numCopies = int(input("How many image files do you need?"))

# User input, set to absolute path name
srcImg = input("Enter the path of the image file you want to copy: ")
srcPath = os.path.abspath(srcImg)


print("Input source: " + srcPath)
print("Input image: " + srcImg)
print("Output folder: " + dstPath)


# Create destination folder
if not os.path.exists(dstPath):
    os.makedirs(dstPath)

os.makedirs('~/Desktop/photoduplicate', )

# Copy file
for i in range(numCopies):
    shutil.copy2(srcImg, '~/Desktop/photoduplicate/{}.png'.format(i))