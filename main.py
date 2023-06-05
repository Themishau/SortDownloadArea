from Pathrunner import Pathrunner
from DirectSorter import DirectSorter
from addpathfile import reads
from adddirectory import readt
def main():
    # Getting the directory
    thisdir = reads()
    targetdir = readt()

    pathrunner = Pathrunner(thisdir, targetdir)

    pathrunner.getRootFilesDirectories()
    pathrunner.getTargetDirectories()
    pathrunner.runThroughFiles()

    directSorter = DirectSorter(pathrunner)
    # directSorter.checkCreateDir()
    directSorter.readDocx()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()



