# 2. Open/Closed Principle (OCP)
#
# Definition: Software entities (classes, modules, functions) should be open for extension
# but closed for modification. This means you should be able to add new functionality
# without changing the existing code.
#
# Example: Consider a class that calculates discounts for different customer types:

class DiscountCalculator:
    def calculate(self, customer_type):
        if customer_type == "Regular":
            return 10
        elif customer_type == "Premium":
            return 20

# This code violates OCP because adding a new customer type requires modifying the existing code.
# To adhere to OCP, we can use polymorphism:

class Discount:
    def calculate(self):
        pass

class RegularDiscount(Discount):
    def calculate(self):
        return 10

class PremiumDiscount(Discount):
    def calculate(self):
        return 20

def get_discount(discount: Discount):
    return discount.calculate()

# Now, if a new discount type is needed, we can create a new class without modifying existing ones.
