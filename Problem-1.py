class Calculator:
    def calculate(self, a, b, operation):
        if operation == 'addition':
            return a + b
        elif operation == 'subtraction':
            return a - b
        elif operation == 'multiplication':
            return a * b
        elif operation == 'division':
            if b == 0:
                return "Cannot divide by zero"
            return a / b
        else:
            return "Invalid operation"

# Example usage
calc = Calculator()
print(calc.calculate(5.0, 3.0, 'addition'))     
print(calc.calculate(5.0, 3.0, 'subtraction'))    
print(calc.calculate(5.0, 3.0, 'multiplication')) 
print(calc.calculate(5.0, 3.0, 'division'))       
