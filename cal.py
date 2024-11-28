import re
import math

def process_factorials_and_powers(expression):
    """
    Replaces instances of 'n!' with 'math.factorial(n)' and 'a^b' with 'math.pow(a, b)' in the expression.
    """
    factorial_pattern = r"(\d+)\!"
    power_pattern = r"(\d+(?:\.\d+)?|\((?:-?\d+(?:\.\d+)?)\))\^(-?\d+(?:\.\d+)?)"

    expression = re.sub(factorial_pattern, r"math.factorial(\1)", expression)
    expression = re.sub(power_pattern, r"math.pow(\1, \2)", expression)

    return expression

def evaluate_expression(expression):
   """
   Switches '!' with the factorial and '^' with powers
   evaluates a mathematical expression string using safe evaluation.
   Returns: result or the error.
   """
   expression = process_factorials_and_powers(expression)
   try:
       result = eval(expression, {"math": math})
       return result
   except ZeroDivisionError:
       return "Error: Division by zero is not allowed."
   except SyntaxError:
       return "Error: Invalid syntax. Please check your input."
   except Exception as e:
       return f"Error: {e}"

def main():
   while True:
       print("If you want to exit, enter 'exit'.")
       user_input = input("Enter an expression: ")


       if user_input.lower() == 'exit':
           break


       result = evaluate_expression(user_input)
       print("Result:", result)


if __name__ == "__main__":
   main()

