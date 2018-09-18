print("This is a tip calculator.")
def tip_calculator(subtotal, percentage):
    tip = subtotal * percentage
    total = subtotal + tip
    return total

input_subtotal = float(input("PLease enter the subtotal of the bill: "))
input_percentage = float(input("Please enter the tip percentage in decimal form: "))

bill_total = tip_calculator(input_subtotal, input_percentage)
print(bill_total)
