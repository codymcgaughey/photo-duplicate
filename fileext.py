
def copyFiles(srcImg, numCopies):
    dstImg = input("Name output folder: ")
    dstImg = "~/Desktop/" + dstImg

    dstImg, file_extension = os.path.splitext(dstImg)

    print(dstImg)
    print(file_extension)

    for i in range(1, numCopies + 1):
        shutil.copy2(srcImg, dstImg + {} + file_extension.format(i))
