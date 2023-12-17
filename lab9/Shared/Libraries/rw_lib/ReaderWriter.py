"""
Utility class for reading user input and writing content to files.
"""


class ReaderWriter:
    def read_input(self, prompt):
        """
        Reads user input with a given prompt.

        Args:
            prompt (str): The prompt to display before reading input.

        Returns:
            str: The user's input.
        """
        return input(prompt)

    def write_output(self, filename, content):
        """
        Writes content to a file with a given filename.

        Args:
            filename (str): The name of the file to write to.
            content (str): The content to write to the file.
        """
        with open(filename, 'w') as f:
            f.write(content)
