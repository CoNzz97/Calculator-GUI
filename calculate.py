import decimal
class Calculate:
    def __init__(self, num_1, num_2, operator):
        try:
            self.num_1 = decimal.Decimal(num_1)
            self.num_2 = decimal.Decimal(num_2)
        except ValueError:
            raise ValueError("Invalid input. Both num_1 and num_2 must be valid numbers.")

        self.result = 0
        self.calculate(operator)

    def calculate(self, operator: str):
        if operator == "+":
            self.add()
        elif operator == "-":
            self.subtract()
        elif operator == "*":
            self.multiply()
        elif operator == "/":
            self.divide()

    def add(self):
        self.result = self.num_1 + self.num_2

    def subtract(self):
        self.result = self.num_1 - self.num_2

    def multiply(self):
        self.result = self.num_1 * self.num_2

    def divide(self):
        if self.num_2 != 0:
            self.result = self.num_1 / self.num_2
        else:
            # Handle division by zero
            raise ValueError("Division by zero is not allowed")

    def equals(self):
        return str(self.result)
