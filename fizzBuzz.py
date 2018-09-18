def fizz_buzz(number):
    if (number % 3 == 0 and number % 5 != 0):
        print("Fizz")
    elif (number % 5 == 0 and number % 3 != 0):
        print("Buzz")
    elif (number % 3 == 0 and number % 5 == 0):
        print("Fizz Buzz")
    else:
        print("¯\_(ツ)_/¯") #no fizz or buzz

input_number = int(input("PLease enter a number: "))
fizz_buzz(input_number)
