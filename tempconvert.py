
user_input = input("To convert farenheit to celsius type F or to convert celsius to farenheit type C: ").upper()
temp_input = int(input("Enter the temperature: "))

def faren_converter(temp):
    cels = ((temp - 32) / 1.8)
    return(cels)

def cels_converter(temp):
    faren = ((temp * 1.8) + 32)
    return faren

def converter(letter_choice):
    result = 0
    if (letter_choice == "F"):
        print("The temperture in celsius is:")
        result = faren_converter(temp_input)
    elif (letter_choice == "C"):
        print("The temperture in farenheit is:")
        result = cels_converter(temp_input)
    return result


answer = converter(user_input)
print(answer)
