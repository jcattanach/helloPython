#name = "John"
#
#names = ["Alex", "John", "Mary", "Steve"]
#
#print(names[0])

#loops
#while


#  def prompt_user_for_input():
#      first_number = int(input("Enter first number: "))
#      second_number = int(input("Enter second number: "))
#      return (first_number, second_number) #tuple
#
#
#  while True:
#
#      choice = input("Enter your choice (+,-,/,*) or q to quit: ")
#
#      if(choice == 'q'):
#          break
#
#      (no1,no2) = prompt_user_for_input()
#
#      if(choice == '+'):
#          print(no1 + no2)
#
#  print("Program quit")


##########################
#dictionaries

#address = {"street" : "1200 Richmond Ave",
#            "city" : "Houston"}

#user_dictionary = {"firstName" : "John",
#                    "lastName" : "Smith",
#                    "address" : address
#                    }


#print(user_dictionary["firstName"])

airports = {"IAH" : "Intercontinental Airport Houston",
            "SEATAC" : "Seattle Airport",
            }

#iterate through dictionary by using loop

#
#
for airport in airports:
    print(airports[airport])
