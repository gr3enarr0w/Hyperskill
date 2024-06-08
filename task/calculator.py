# Print the earned amount for the store
print("Earned Amount:")
print("Bubblegum: $202")
print("Toffee: $118")
print("Ice cream: $2250")
print("Milk chocolate: $1680")
print("Doughnut: $1075")
print("Pancake: $80")
print("")

income = float(5405.00)
print("Income: $" + str(income))

staff_expenses = float(input("Staff expenses: "))
other_expenses = float(input("Other expenses: "))

print("Staff expenses: $", staff_expenses, sep="")
print("Other expenses: $", other_expenses, sep="")

net_income = income - (staff_expenses + other_expenses)
print("Net Income: $", net_income, sep="")

if __name__ == '__main__':
    pass