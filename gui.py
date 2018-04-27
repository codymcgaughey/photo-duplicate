from tkinter import *
from tkinter import filedialog
import os
import shutil
import subprocess
import platform

# Constants
OSPATH = os.path.abspath('~/Desktop/photoduplicate')

# TK
root = Tk()
filenamedisplay = StringVar()
root.title("Photo Duplicate")

# Functions

def open_file(OSPATH):
    if platform.system() == "Windows":
        os.startfile(OSPATH)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", OSPATH])
    else:
        subprocess.Popen(["xdg-open", OSPATH])

# WORKING
def get_file(event):
    global fileamount
    fileamount = numImagesEntry.get()
    fileamount = int(fileamount)

    global filename
    filename = filedialog.askopenfilename(initialdir = "Desktop/",
                                               title = "Select file",
                                               filetypes = (("jpeg files","*.jpg"),
                                                            ("png files","*.png"),
                                                            ("all files","*.*")))
    return filename

#WORKING
def get_num(event):
    global fileamount
    fileamount = numImagesEntry.get()
    fileamount = int(fileamount)


# Copy Files
def copy_files(event):
    os.makedirs('~/Desktop/photoduplicate')
    for i in range(1, fileamount + 1):
       shutil.copy2(filename, '~/Desktop/photoduplicate/{:02}.png'.format(i))
    print("submitted")
    open_file(OSPATH)

#####
# Layout

# TODO
# Remove entry for path, replace with text field that shows path
# Show number of copies to be made
# Clean up source code
# Add image format extensions

# Frames
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

# Labels
numImagesLabel = Label(bottomFrame, text="Number of copies: ")
numImagesLabel.grid(row=1, sticky=E)

srcPathLabel = Label(bottomFrame, text="Path of image file: ")
srcPathLabel.grid(row=2, sticky=E)

# Entries
numImagesEntry = Entry(bottomFrame)
numImagesEntry.grid(row=1, column=1)

srcPathDisplay = Label(bottomFrame, )
srcPathDisplay.grid(row=2, column=1)

# Buttons
numButton = Button(bottomFrame, text="Submit Number")
numButton.grid(row=1, column=2)
numButton.bind("<Button-1>", get_num)

srcPathButton = Button(bottomFrame, text="Select File")
srcPathButton.bind("<Button-1>", get_file)
srcPathButton.grid(row=2, column=2, sticky=(W,E))

# Add function to make copies, open directory
submitButton = Button(bottomFrame, text="Submit Images")
submitButton.bind("<Button-1>", copy_files)
submitButton.grid(row=3, column=2, sticky=(W,E))


root.mainloop()