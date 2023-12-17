class History:
    """
    The History class keeps track of queries and their results.
    """

    def __init__(self):
        """
        Initializes a History object with an empty history and a query ID of 0.
        """
        self.history = []
        self.query_id = 0

    def add_to_history(self, query, result):
        """
        Adds a query and its result to the history.
        """
        self.query_id += 1
        self.history.append((self.query_id, query, result))

    def view_history(self):
        """
        Prints the history of queries and their results.
        """
        for item in self.history:
            print(f"{item[0]}. Query: {item[1]}, Result: {item[2]}")
