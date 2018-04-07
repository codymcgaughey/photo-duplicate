import os.path
import shutil


# Default folder destination is desktop
def PATHWAY():
    return '~/Desktop'


# Check if destination path exists, create if not:
def GetOutputFolder(defaultpath):
    print("Folder already exists on desktop.")
    folder = input("Choose a new folder name: ")
    result = os.path.join(defaultpath, folder)
    return result

#######


def main():

    defaultpath = PATHWAY()

    # Get info from user:
    IMGPATH = input("Enter the path of the image you want to copy: ")
    COPIES = input("Enter number of copies: ")
    folder = input("Name the folder where these images will be stored: ")

    # Join default path & folder name
    folderpath = os.path.join(defaultpath, folder)
    print(folderpath)

    # # Check for existing folder name
    # folderpath = GetOutputFolder(defaultpath, folderpath)

    # Create Output Folder
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)


main()
