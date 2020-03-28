"""Module for handling user input when we want to replace tabs in a folder."""

from os import listdir
from os.path import isfile, join


class Replacer():
    """Class for handling tab replacement for files in a folder."""

    def __init__(self):
        """Constructor method.

        Calls the getParameters() function to set the required values.

        Attributes:
            _tabSpace (String): The amount of spaces that a tab represents.
            _folderPath (String): The folder containing the files to alter.
            _fileType (String): The types of files that are to be altered.

        Raises:
            FileNotFoundError: Invalid file or folder.
            SystemExit: Exit if the user wishes to.
        """

        self._tabSpace = ''
        self._folderPath = ''
        self._fileType = ''

        self.setParameters()

    def setParameters(self):
        getTabSpaces = input("How many spaces are tabs? (4 or 8): ")
        while(getTabSpaces not in ['4', '8']):
            getTabSpaces = input("How many spaces are tabs? (4 or 8): ")

        self._tabSpace = ' ' * int(getTabSpaces)
        self._folderPath = input("The absolute path of the folder: ")

        self._fileType = input("Provide a file extension "
                               "(txt, doc, sql, ...): ")
        while(self._fileType not in ['txt', 'doc', 'sql']):
            self._fileType = input("Provide a file extension "
                                   "(txt, doc, sql, ...): ")

    def _showParameters(self):
        """Method to display the current parameters."""

        print("Please check the parameters ... \n")
        print("Tabs replaced with: " + str(len(self._tabSpace)) + " spaces")
        print("In the folder: " + self._folderPath)
        print("Alter these file types: '" + self._fileType)

    def verify(self):
        """This method exists to verify whether the settings are correct.

        The user can provide one of 3 inputs. 'y' to accept the parameters
        and replace the contents of the file. 'n' uf the user rejects the
        given parameters, in which case then the getParameters() method is
        run again. 'q' of the user wants to quit the program.

        Returns: True if we receive user confirmation, False if not, and
                 raises a SystemExit, otherwise.
        """

        self._showParameters()
        isReady = input("Proceed with replacement? (y/n/q): ")
        while(isReady not in ['y', 'n', 'q']):
            isReady = input("Proceed with replacement? (y/n/q): ")
        if(isReady == 'y'):
            return True
        elif(isReady == 'n'):
            return False
        elif(isReady == 'q'):
            raise SystemExit

    def replace(self):
        """Method for replacing certain files in a folder.

        First we create a list of all files with the matching file extention.
        Then for each file we open, read, replace, and write.

        Raises:
            FileNotFoundError: There was a problem reading a file(s).
        """

        try:
            targetFiles = [files for files in listdir(self._folderPath)
                           if isfile(join(self._folderPath, files)) and
                           files[-len(self._fileType):] == self._fileType]
            targetFiles = [self._folderPath + "\\" + x for x in targetFiles]
            for f in targetFiles:
                myFile = open(f, 'r')
                tabsReplaced = myFile.read()
                tabsReplaced = tabsReplaced.replace('\t', self._tabSpace)

                myFile = open(f, 'w')
                myFile.write(tabsReplaced)
                myFile.close()
            print("Finished tab replacement.")

        except FileNotFoundError:
            print("Error: There was a problem with the directory.")
            return
