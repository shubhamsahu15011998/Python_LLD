# 5. Dependency Inversion Principle (DIP)
#
# Definition: High-level modules should not depend on low-level modules;
# both should depend on abstractions. Abstractions should not depend on details;
# details should depend on abstractions.
#
# Example: Suppose you have a LightBulb class that depends on a Switch class:

class LightBulb:
    def turn_on(self):
        print("Light is on")

    def turn_off(self):
        print("Light is off")

class Switch:
    def __init__(self, bulb: LightBulb):
        self.bulb = bulb

    def operate(self, on):
        if on:
            self.bulb.turn_on()
        else:
            self.bulb.turn_off()

# Here, Switch depends directly on the LightBulb class.
# This makes it difficult to replace LightBulb with other types of lights.
# To adhere to DIP, use an abstraction:

class Switchable:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        print("Light is on")

    def turn_off(self):
        print("Light is off")

class Switch:
    def __init__(self, device: Switchable):
        self.device = device

    def operate(self, on):
        if on:
            self.device.turn_on()
        else:
            self.device.turn_off()

# Now, Switch depends on the Switchable interface, allowing any switchable
# device to be used without changing the Switch class.
