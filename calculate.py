class Calculate:
    def __init__(self, num_1, num_2, operator):
        num_1 = float(num_1)
        num_2 = float(num_2)
        self.result = 0

        if operator == "+":
            self.add(num_1, num_2)
        elif operator == "-":
            self.subtract(num_1, num_2)
        elif operator == "*":
            self.multiply(num_1, num_2)
        elif operator == "/":
            self.divide(num_1, num_2)

    def add(self, num_1, num_2):
        self.result = num_1 + num_2

    def subtract(self, num_1, num_2):
        self.result = num_1 - num_2

    def multiply(self, num_1, num_2):
        self.result = num_1 * num_2

    def divide(self, num_1, num_2):
        if num_2 != 0:
            self.result = num_1 / num_2
        else:
            # Handle division by zero
            self.result = "Error"

    def equals(self):
        return str(self.result)
