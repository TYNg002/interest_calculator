import math

# Check if input can be casted to float
# If not, print prompt and ask for input again
def float_check(question):
    while True:
        try:
            item = float(input(question))
            break
        except ValueError:
            print("Please enter a number.")
    return item

# Ask user to choose loan or investment - using tab escape characters to make presentable
print("Choose either 'investment' or 'loan' from the menu below to proceed:")
print("investment\t-\tto calculate the amount of interest you'll earn on your investment")
calculation = input("loan\t\t-\tto calculate the amount you'll have to pay on a loan\n")
# Convert input to lowercase to enable usage of user input regardless of capitalisation
calculation = calculation.lower()

# Display error message if input not recognised
while not (calculation == "loan" or calculation == "investment"):
    calculation = input("Error: Input was not recognised. Please enter 'investment' or 'loan'.\n")

# This is the investment section
if calculation == "investment":
    # Ask for deposit amount
    deposit = float_check("\nHow much will you be depositing?\n")

    # Ask for interest rate
    interest_percentage = float_check("\nWhat percentage is the interest?\n")
    interest_rate = interest_percentage / 100
    # Ask for investment duration
    duration_years = float_check("\nHow many years will you be investing for?\n")

    # Ask for interest type
    interest_type = input("""\nWould you like to calculate interest based on simple or compound 
interest? (simple / compound)\n""")
    interest_type = interest_type.lower()
    # Display error message if input not recognised
    while not (interest_type == "simple" or interest_type == "compound"):
        interest_type = input("Error: Input was not recognised. Please enter 'simple' or 'compound'.\n")
        interest_type = interest_type.lower()

    # Calculate simple interest
    if interest_type == "simple":
        interest_amount = deposit * (1 + interest_rate * duration_years)

    # Calculate compound interest
    else:
        interest_amount = deposit * math.pow((1 + interest_rate), duration_years)

    # Print amount
    print(f"\nThe total at the end of the investment duration is {round(interest_amount,2)}.")

# This is the loan section
else:
    # Ask for house value
    value = float_check("\nHow much is the current value of the loan?\n")

    # Ask for interest rate
    interest_percentage = float_check("\nWhat percentage is the interest?\n")
    interest_rate_monthly = interest_percentage / 100 / 12
    # Ask for loan duration
    duration_months = float_check("\nHow many months do you plan to take to repay the loan?\n")

    # Calculate loan repayment
    repayment = (interest_rate_monthly * value) / (1 - (1 + interest_rate_monthly) ** (-duration_months))

    # Print repayment
    print(f"\nThe repayment each month will be {round(repayment, 2)}.")