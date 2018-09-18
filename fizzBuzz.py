def fizz_buzz(number):
    if (number % 3 == 0 and number % 5 != 0):
        print("Fizz")
    elif (number % 5 == 0 and number % 3 != 0):
        print("Buzz")
    elif (number % 3 == 0 and number % 5 == 0):
        print("Fizz Buzz")

input_number = int(input("PLease enter a number: "))
fizz_buzz(input_number)
