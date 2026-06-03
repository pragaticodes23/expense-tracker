print('======EXPENSE CALCULATOR======')
Total_amount=float(input("Enter total amount:"))
Food=float(input("Enter expenditure on food:"))
Travel=float(input("Enter expenditure on travelling:"))
Shopping=float(input("Enter expenditure on shopping:"))
Entertainment=float(input("Enter expenditure on Entertainment:"))

Total_spent=Food+Travel+Shopping+Entertainment          #Calculating total amount spent

Balance_left=Total_amount-Total_spent                   #Calculating balance amount left

print('Total amount spent is:',Total_spent)

print('Total balance amount left is:',Balance_left)

print("Thank you for using EXPENSE CALCULATOR")
