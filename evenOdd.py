print("This function calculates if a number is EVEN or ODD.")
def even_odd(num):
    if (num % 2 == 0):
        print("EVEN")
    else:
        print("ODD")

input_num = int(input("Enter a number: "))

even_odd(input_num)
