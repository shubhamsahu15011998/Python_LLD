# 4. Interface Segregation Principle (ISP)
#
# Definition: A client should not be forced to implement interfaces they do not use.
# This means it's better to have many smaller, specific interfaces than one large, general-purpose interface.
#
# Example: Suppose you have an interface Printer:

class Printer:
    def print(self):
        pass

    def scan(self):
        pass

    def fax(self):
        pass

# A SimplePrinter class that only needs to print would have to implement methods it doesn’t use:

class SimplePrinter(Printer):
    def print(self):
        print("Printing...")

    def scan(self):
        pass  # Not needed

    def fax(self):
        pass  # Not needed

# This violates ISP. A better approach is to create smaller interfaces:

class Printable:
    def print(self):
        pass

class Scannable:
    def scan(self):
        pass

class Faxable:
    def fax(self):
        pass

class SimplePrinter(Printable):
    def print(self):
        print("Printing...")

# Now, classes implement only the methods they need.

