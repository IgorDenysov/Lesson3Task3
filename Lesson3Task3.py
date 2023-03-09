first_variable = float(int(input('Enter first number: ')))
second_variable = float(int(input('Enter second number: ')))
add = first_variable + second_variable
sub = first_variable - second_variable
division = first_variable / second_variable
multiplication = first_variable * second_variable
exponent = first_variable ** second_variable
modulus_first = abs(first_variable)
modulus_second = abs(second_variable)
floor_division = first_variable // second_variable
str = " of these numbers is: "
print('Sum', str, add)
print('Subtraction', str, sub)
print('Division', str, division)
print('Multiplication', str, multiplication)
print('Exponent', str, exponent)
print('Modulus', str, modulus_first, ' and ', modulus_second)
print('Floor division', str, floor_division)