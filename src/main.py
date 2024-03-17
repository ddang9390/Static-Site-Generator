from textnode import TextNode
import os, shutil

def main():
    static_to_public()

def static_to_public():
    shutil.rmtree(path="../public")
    if not os.path.exists("../public"):
        os.mkdir("../public")

    if os.path.exists("../static"):
        copyFiles("../static", "../public")

    


def copyFiles(source, destination):
    if not os.path.exists(destination):
         os.mkdir(destination)

    for file in os.listdir(source):
            filePath = os.path.join(source, file)
            destPath = os.path.join(destination, file)
            if os.path.isfile(filePath):
                print(filePath)
                
                shutil.copy(filePath, destPath)
            else:
                copyFiles(filePath, destPath)

main()