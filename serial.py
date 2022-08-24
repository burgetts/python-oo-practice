"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """Initializes index as the start number."""
        self.index = start
        

    def generate(self):
        """ Generates and returns the next sequential number. """
        self.index += 1
        return self.index-1
    
    def reset(self):
        """ Resets index to 100. Returns None. """
        self.index = 100

