# Sequential FLow
- Data is passed down through the algorithm using variables.
- * Variable: way to refer to a place in memory where a value can be stored without having to use the memory address.
- In python variables are referred to as identifiers
  
# Rules for identifiers:
- must start with lowercase, uppercase, or underscore
- rest of the identifier can eb any combo of symbols
- cannot have whitespaces
- cannot be any python keywords
  
- Python is case-sensitive
  
- is good practice to use identifiers that reflect the purpose of the variable (readability)

# Python keywords
- False
- None
- True
- and 
- as 
- assert
- async
- await
- break
- class
- continue
- def
- del
- elif
- else
- except
- finally
- for
- from
- global
- if
- import
- in
- is
- lambda
- nonlocal
- not
- or
- pass
- raise
- return
- try
- while
- with
- yield

# Data types
- Integer --> int()
- Float (decimal) --> float()
- String --> str()
- Boolean --> bool()

- Variables are automatically siigned or changed to the type of variable based on the value stored or you can manually force a change in type using the convert functions.

# Basic math operators:
High precedence:
- Power: **

Medium precedence:
- Multiplication: * 
- Division: /
- Integer division: "//" note: divides and keeps the whole number part
- Modulus: %

Low Precedence:
- Addition: +
- Subtraction: -

# Order of precedence rules: 
1. Perform all operations within parentheses
2. Perform all operations at the high level
3. Perform all operations at the medium level
4. Perform all operations at the low level

# Advanced math operations
- Use the math library
- 'import math'
- >>> math.sin() math.pi math.exp math.fabs and so on and so forth
- https://docs.python.org/3/library/math.html

# Inputs
- 'input' function is used to prompt the user for a value
- By default, the 'input' command provides a string of what is entered by the user

- Example prompt for a decimal number: x = float(input('Please enter a decimal number: '))

# Outputs
- 'print' function
- >>> a = 111
- >>> h = 1.24
- >>> n = 'Bilbo baggins'
- >>> print('{0} is {1} years old and {2:0.2f} m tall.\n'.format(n,a,h))
- Note: {2:0.2f} tells the float value of 'h' at index=2 to use two decimal places instead of the default one decimal place.

# Conditional flow
- # Operators
- equal: ==
- not equal: !=
- greater than: >
- less than: <
- greater than or equal to: >=
- less than or equal to: <=