"""Module for handling user input when we want to replace tabs in a file."""


class Replacer():
    """Class for handling tab replacement for a single file."""

    def __init__(self):
        """Constructor method.

        Calls the getParameters() function to set the required values.

        Attributes:
            _tabSpace (String): A string with the appropriate amount of spaces.
            _filePath (String): The file that is to be changed.

        Raises:
            FileNotFoundError: Invalid file.
            SystemExit: Exit if the user wishes to.
        """

        self._tabSpace = ''
        self._filePath = ''

        self.setParameters()

    def setParameters(self):
        """Method for getting the user input on what they wish to alter."""

        getTabSpaces = input("How many spaces are tabs? (4 or 8): ")
        while(getTabSpaces not in ['4', '8']):
            getTabSpaces = input("How many spaces are tabs? (4 or 8): ")
        self._tabSpace = ' ' * int(getTabSpaces)

        self._filePath = input("Provide the absolute filepath: ")

    def _showParameters(self):
        """Method to display the current parameters."""

        print("Please check the parameters ... \n")
        print("Tabs replaced with: " + str(len(self._tabSpace)) + " spaces")
        print("File to alter: '" + self._filePath + "'")

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
        """Method for replacing tabs in a file with spaces.

        This is done by way of: read, replace, write.

        Raises:
            FileNotFoundError: The file is invalid.
        """

        try:
            myFile = open(self._filePath, 'r')
            tabsReplaced = myFile.read()
            tabsReplaced = tabsReplaced.replace('\t', self._tabSpace)

            myFile = open(self._filePath, 'w')
            myFile.write(tabsReplaced)
            myFile.close()
            print("Finished tab replacement.")

        except FileNotFoundError:
            print("Error: The file " + self._filePath + " was not found.")
            return
