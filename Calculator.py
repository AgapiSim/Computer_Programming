"""
Student: Agapi Eleni Simaiaki
Reviewed date: 19/09/2023
Part of the course: Computer programming II (1TD722)
Uppsala University
"""

"""
Module 2: Recursive descent, exceptions, function objects and more
Build a calculator which reads and calculates arithmetic expressions.
Concepts covered: parsing with ”recursive descent”, exceptions, function objects.
Use with the provided wrapper class TokenizeWrapper: MA2tokenizer.py
"""


import math
from tokenize import TokenError
from MA2tokenizer import TokenizeWrapper


class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


class EvaluationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)



######### Globally define dictionaries to map function names to functions  ###########
math_functions = {"sin": math.sin, "log": math.log, "cos": math.cos, "exp": math.exp}
gen_functions = {"min": min, "max": max, "mean": (lambda x: sum(x) / len(x)), "sum": sum}



def statement(wtok, variables):
    #Might need an if statement for EOL but it works
    result = assignment(wtok, variables)
    return result



def assignment(wtok, variables):
    result = expression(wtok, variables)

    #Helps check later if not other assignment exists
    flag = False 

    while wtok.has_next() and wtok.get_current() == '=': 
        # Escape the '=' 
        wtok.next()

        # Check if the next character is a valid variable 
        if not wtok.is_name():
            raise SyntaxError("Expected a valid variable name")

        else:
            var_name = wtok.get_current()
            # Append/update dictionary of variables with the new ones
            variables[var_name] = result
            flag = True
            #Get next character and check for assignment or error
            wtok.next()     

    #Could be written more simple 
    if flag and wtok.has_next():
        if not wtok.get_current().isalpha() and wtok.get_current()!=")":
                raise SyntaxError("Expected a valid variable name")
    
    return result



def expression(wtok, variables):
    result = term(wtok, variables)
    
    while wtok.get_current() in ('+', '-'):
        #save operator to determine how to proceed
        operator = wtok.get_current()
        wtok.next()
        if operator == '+':
            result += term(wtok, variables)
        else:
            result -= term(wtok, variables)
    
    return result



def term(wtok, variables):
    result = factor(wtok, variables)

    while wtok.get_current() in ('*', '/'):
        operator = wtok.get_current()
        wtok.next()
        factor_result = factor(wtok, variables)
        if operator == '*':
            result *= factor_result
        elif operator == '/':
            if factor_result == 0:
                raise EvaluationError("Division by zero")
            result /= factor_result
    
    return result



def factor(wtok, variables):
    
    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'")
        wtok.next()   
    
    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()
    
    #make sure - maintained and not passed
    elif wtok.get_current() == "-":
        wtok.next()
        if wtok.get_current() == "(":
            wtok.next()
            result = -assignment(wtok, variables)
        elif wtok.is_number():
            result = -float(wtok.get_current())
            wtok.next()
    
    elif wtok.is_name():
        if wtok.get_current() in variables:
            result = variables[wtok.get_current()]
            wtok.next()

        #too ugly but works
        elif wtok.get_current() in math_functions or  wtok.get_current() in gen_functions or wtok.get_current() in ('fib' , 'fac'):
            function_name = wtok.get_current()
            wtok.next()
            if wtok.get_current() != '(':
                raise SyntaxError("Expected '(' after function name")
            wtok.next()
            arguments = []
            while wtok.get_current() != ')':
                arguments.append(assignment(wtok, variables))
                #print(arguments)
                if wtok.get_current() == ',':
                    wtok.next()
                elif wtok.get_current() != ')':
                    raise SyntaxError("Expected ',' or ')' in function arguments")
            wtok.next()
            result = evaluation_function(function_name,arguments)
        else:
            raise EvaluationError("Variable is undefined")

    else:
        raise SyntaxError("Expected number, function, or variable")
    
    return result



def evaluation_function(function_name, arguments):
    if function_name in math_functions:
        #Make sure Evaluation Error is raised in log
        if function_name == 'log':
            n = arguments[0]
            if n < 0:
                raise EvaluationError(f"Argument to log is {n}. Must be an integer >= 0")
            return math_functions[function_name](arguments[0])
        return math_functions[function_name](arguments[0])
        
    elif function_name in gen_functions:
        result = gen_functions[function_name](arguments)
        return result
    
    elif function_name == 'fib':
        n = int(arguments[0])
        if n < 0:
            raise EvaluationError(f"Argument to fib is {n}. Must be an integer >= 0")
        return fibonacci(n)
    elif function_name == 'fac':
        n = arguments[0]
        if n < 0 or n != int(n):
            raise EvaluationError(f"Argument to fac is {n}. Must be an integer >= 0")
        return factorial(n)
    else:
        raise EvaluationError(f"Unknown function: {function_name}")



#Recursive function from MA1 is very slow to use
def fibonacci(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b



#Recursive function from MA1
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)



def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file
    """
    
    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
    # Note: The unit test file initiates variables in this way. If your implementation 
    # requires another initiation, you have to update the test file accordingly.
    init_file = 'MA2init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0]=='#':
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()
        elif wtok.get_current() == 'vars':
            print_variable_values(variables)
        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result)
            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")
            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')

if __name__ == "__main__":
    main()
