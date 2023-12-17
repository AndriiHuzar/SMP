class ErrorHandler:
    """
    The ErrorHandler class handles errors that occur when calling a function.
    """
    @staticmethod
    def handle_error(func):
        """
        Handles errors that occur when calling the function 'func'.
        """
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Error: {e}")
                return [], [], [], []  # return empty lists

        return wrapper
