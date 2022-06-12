class BaseException(Exception):
    """Global exception class for Invera."""

    def __init__(self, message=None):
        """Do something useful with extra params."""
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
        self.message = message
