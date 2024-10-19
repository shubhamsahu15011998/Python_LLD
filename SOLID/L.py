# 3. Liskov Substitution Principle (LSP)
#
# Definition: Objects of a superclass should be replaceable with objects of a subclass
# without affecting the correctness of the program.
#
# Example: Consider a superclass Bird and a subclass Penguin:

class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying")

class Penguin(Bird):
    def fly(self):
        print("Penguin can't fly")

# Here, substituting Penguin for Bird will break the code since Penguin cannot fly. This violates LSP. A better approach is to use a separate interface for flying:

class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        pass

class Sparrow(FlyingBird):
    def fly(self):
        print("Sparrow is flying")

class Penguin(Bird):
    def swim(self):
        print("Penguin is swimming")

# Now, Penguin does not inherit the fly method, adhering to LSP.
