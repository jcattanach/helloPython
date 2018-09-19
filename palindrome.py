print("This function determines if text is a palindrome or not")

user_input = input("Enter a string: ").lower()

def reverse_string(string):
    reverse = ""
    for index in range(len(string) -1, -1, -1):
        reverse = reverse + string[index]
    return reverse

input_reversed = reverse_string(user_input)

def is_palindrome(string):
    result = "The string is NOT a palindrome."
    if(input_reversed == string):
        result = "The string IS a palindrome."
    return result

answer = is_palindrome(user_input)
print(answer)
