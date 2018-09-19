print("This Module determines the factorial of a number")

user_number = int(input("Enter a number: "))
final = 1

for number in range(1,user_number + 1):
    final = final * number


print(final)
