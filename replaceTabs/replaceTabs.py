"""A module for replacing tabs in a file with 4 or 8 spaces."""


from replaceTabs.replacementOptions import replaceInFile
from replaceTabs.replacementOptions import replaceInFolder


def main():
    """Main method.

    Gets two inputs from the user. The first is the number of spaces a tab
    represents, and the other is whether to replace tabs in a single file or
    an entire directory.
    """

    getInputFormat = input('Single file (s) or folder (f): ')
    while(getInputFormat not in ['s', 'f']):
        getInputFormat = input('Single file (s) or folder(f): ')

    parameters = None
    if(getInputFormat == 's'):
        parameters = replaceInFile.Replacer()
    elif(getInputFormat == 'f'):
        parameters = replaceInFolder.Replacer()
    else:
        print("Something went wrong ...")
        return

    try:
        while(not parameters.verify()):
            print("Restarting...\n")
            parameters.setParameters()
    except SystemExit:
        print("Exiting...")
        return
    parameters.replace()
