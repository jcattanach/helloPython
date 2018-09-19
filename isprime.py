print("This function determines if a number is prime.")

def is_prime(num):
    result = "Number is NOT prime"
    if(num % 2 == 0 and num != 2):
        return result
    elif(num % 3 == 0 and num != 3):
        return result
    elif(num % 5 == 0 and num != 5):
        return result
    elif(num % 7 == 0 and num != 7):
        return result
    elif(num == 1):
        return result
    else:
        result = "Number IS prime"
        return result

prime_input = int(input("Enter a number: "))

result = is_prime(prime_input)
print(result)
