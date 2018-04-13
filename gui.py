from tkinter import *
from tkinter import filedialog
import os
import shutil
import subprocess
import platform

OSPATH = os.path.abspath('~/Desktop/photoduplicate')


root = Tk()



root.title("Photo Duplicate")
#####
# Functions

def printName(event):
    print("hello")

#def open_file(event):
 #   if platform.system() == "Windows":
  #      os.startfile(OSPATH)
   # elif platform.system() == "Darwin":
    #    subprocess.Popen(["open", OSPATH])
   # else:
    #    pass

# WORKING
def getFile(event):
    global filename
    filename = filedialog.askopenfilename(initialdir = "Desktop/",
                                               title = "Select file",
                                               filetypes = (("jpeg files","*.jpg"),
                                                            ("png files","*.png"),
                                                            ("all files","*.*")))

    return filename

#WORKING
def getNum(event):
    global fileamount
    fileamount = numImagesEntry.get()



#####
# Layout

# TODO
# Edit Button Size, move submit to right side
# Remove entry for path, replace with text field that shows path
# Add functionality for submit
# Add functionality to open output folder
# Let user choose output folder
# Clean up source code
#

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

numImagesLabel = Label(bottomFrame, text="Number of copies: ") # text field descriptor
srcPathLabel = Label(bottomFrame, text="Path of image file: ") # text field descriptor


numImagesEntry = Entry(bottomFrame) # input
srcPathEntry = Entry(bottomFrame, ) # input


submitButton = Button(bottomFrame, text="Submit Images") # display button
submitButton.bind("<Button-1>", printName) # activate button, printName = function

numButton = Button(bottomFrame, text="Submit Number")
numButton.grid(row=1, column=2)
numButton.bind("<Button-1>", getNum)

numImagesLabel.grid(row=1, sticky=E) # display descriptor
numImagesEntry.grid(row=1, column=1) # display entry field

srcPathLabel.grid(row=2, sticky=E)
srcPathEntry.grid(row=2, column=1)

# Add function to open directory
srcPathButton = Button(bottomFrame, text="Select File")
srcPathButton.bind("<Button-1>", getFile)
srcPathButton.grid(row=2, column=2, sticky=E)


submitButton.grid(row=3, column=2, sticky=E) # display button




root.mainloop()