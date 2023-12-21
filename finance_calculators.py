import math

while True:
    calculation_type = input("Do you want to calculate return on an investment (I) or \
the amount you'll pay on a home loan (B)?: ").lower()

    if calculation_type == "i":
        while True:
            try:
                investment = int(input("Enter investment amount (£): "))
                break 
            except ValueError:
                print("Entry invalid, please enter a number.")

        while True:
            try:
                interest = float(input("What is your interest rate? (%): "))/100
                break
            except ValueError:
                print("Entry invalid, please enter a percentage in numbers.")

        while True:
            try:
                years = int(input("How many years will you invest?: "))
                break
            except ValueError:
                print("Entry invalid, please enter a number of years")
        
        while True:
            interest_type = input("Do you want simple (S) or compound (C) interest? ").lower()

            if interest_type == "c":
                total_amount = float(investment * math.pow((1 + interest), years)) # Compound interest formula
                print(f"The total amount of your investment, using compound interest will be:\
                      £{round(total_amount, 2)}")
                break 
    
    
            elif interest_type == "s":
                simple_interest = float(investment) * (1 + interest * years) # Simple interest formula 
                print(f"The total amount of your investment, using simple interest will be:"
                      f"£{round(simple_interest)}")
                break

            else:
                print("Invalid entry, please select one of the available options (S) or (C)")
    

    elif calculation_type == "b":
        while True:
            try:
                house_value = int(input("What is the value of your home? (£): "))
                break
            except ValueError:
                print("Entry invalid, please enter the value in pounds")

        while True:
            try:
                interest_rate = float(input("What is the interest rate on your loan? (%): "))
                break
            except ValueError:
                print("Entry invalid, please enter a percentage in numbers.")

        while True:
            try:
                repayment_length = int(input("How long will you need to repay the loan (months): "))
                break
            except ValueError:
                print("Entry invalid, please enter the number of months.")

        monthly_interest = float((interest_rate / 100) / 12)

        repayment_amount = int(monthly_interest * house_value) / (1 - (1 + monthly_interest) ** (0 - repayment_length)) 
    
        print(f" Your monthly repayments will total: £{round(repayment_amount, 2)}")

    # Make sure the user only selects available options
    else:
        print("Please select one of the available options (I) or (B)")