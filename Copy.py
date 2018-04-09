import os.path
import shutil


# Default folder destination is desktop
def dstDefault():
    return '~/Desktop'


# Check if destination path exists, create if not:
def getOutputFolder(defaultpath):
    print("Folder already exists on desktop.")
    folder = input("Choose a new folder name: ")
    result = os.path.join(defaultpath, folder)
    return result


# Rename Files

#######



def main():

    # NAMELENGTH = 3
    defaultpath = dstDefault()

    # Get info from user:
    IMGPATH = input("Enter the path of the image you want to copy: ")
    COPIES = input("Enter number of copies: ")
    copieslength = int(COPIES)
    print(copieslength)
    folder = input("Name the folder where these images will be stored: ")

    # Join default path & folder name
    folderpath = os.path.join(defaultpath, folder)
    print(folderpath)


    # Create Output Folder
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)

    # Make copies of Images
    shutil.copy2(IMGPATH, folderpath)

    # Move to new folder
    os.chdir(folderpath)

    for i in range(100):
        shutil.copy2(folderpath, )


main()
