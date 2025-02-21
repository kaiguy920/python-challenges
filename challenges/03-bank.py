# print("Welcome to Chase bank.")
# print("Have a nice day!")

# ### Challenge 3 - Bank Transactions
# Create a prompt that asks the user if they would like to display their balance,
# withdraw or deposit. Write three methods to perform these calculations and
# output the result to the user.

# Gather user input using the `input` function. Note that input always returns
# user input as a string. You have to manually convert it to an int or a float
# to make it behave like number. Also, end the input prompt with a \n newline
# character if you want the user to type in on the next line.

# ```
# age = input("How old are you?\n")
# age = int(age)
# ```

# Here is a sample output:

# ```
# Your current balance is
# 4000
# What would you like to do? (deposit, withdraw, check_balance)
# deposit
# How much would you like to deposit?
# 1000
# Your current balance is 5000
# Are you done?
# yes
# Thank you!
# ```
print("Welcome to Chase bank.")
current_balance = 4000
option = input(
    "What  would you like to do? (deposit, withdraw, check_balance)")

if (option == "check_balance"):
    print(current_balance)
elif (option == "withdraw"):
    withdraw = int(input("how much would you like to withdraw?"))
    print(f"your current balance is: {current_balance - withdraw}")
elif (option == "deposit"):
    deposit = int(input("how much would you like to deposit?"))
    print(f"your current balance is: {current_balance + deposit}")
else:
    response = input("Are you done?")
    if response == "yes":
        print("thank you!")
    else:
        print("please start at the beginning to prompt your new withdraw, deposit or to check_balance")
