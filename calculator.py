from mathFunctions import add_function, sub_function, mul_function, div_function

#calculator function

print("This function is a basic calculator.")
def calculator(first_number, operator, second_number):
    if (operator == '+'):
        return add_function(first_number, second_number)
    elif (operator == '-'):
        return sub_function(first_number, second_number)
    elif (operator == '/'):
        return div_function(first_number, second_number)
    elif (operator == '*'):
        return mul_function(first_number, second_number)
    else:
        print("Please enter a valid operator.")

input_first_num = int(input("Enter a number: "))
input_operator = input("Enter a mathmatical operator (+,-,/,*): ")
input_second_num = int(input("Enter a number: "))

result = calculator(input_first_num, input_operator, input_second_num)
print(result)
