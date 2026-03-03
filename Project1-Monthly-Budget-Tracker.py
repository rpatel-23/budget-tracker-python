def calculate_monthly_income():
    monthly_income = None
    while True:
        monthly_income = input('What is monthly income?')
        try:
            monthly_income = float(monthly_income)
        except:
            print('Invalid Input')
            continue
        if monthly_income < 0:
            print('Put Positive Value')
            continue 
        monthly_income = round(monthly_income, 2)
        return(monthly_income)        
def calculate_monthly_expenses():
    monthly_expenses_amount = None    
    while True:
        rent_expenses = input("What are monthly rent expenses?")
        food_expenses = input("What are monthly food expenses?")
        transportation_expenses = input("What are monthly transportation expenses?")
        clothing_expenses = input("What are monthly clothing expenses?")
        leisure_expenses = input("What are monthly leisure expenses?")
        try:
            rent_expenses = float(rent_expenses)
            food_expenses = float(food_expenses)
            transportation_expenses = float(transportation_expenses)
            clothing_expenses = float(clothing_expenses)
            leisure_expenses = float(leisure_expenses)
        except:
            print('Invalid Input')
            continue
        if rent_expenses < 0:
                print('Put Positive Value')
                continue
        elif food_expenses < 0:
                print('Put Positive Value')
                continue
        elif transportation_expenses < 0:
                print('Put Positive Value')
                continue
        elif clothing_expenses < 0:
                print('Put Positive Value')
                continue
        elif leisure_expenses < 0:
                print('Put Positive Value')
                continue
        else:
             break
    expenses = (rent_expenses + food_expenses + transportation_expenses + clothing_expenses + leisure_expenses)
    monthly_expenses_amount = expenses
    monthly_expenses_amount = round(monthly_expenses_amount, 2)
    return(monthly_expenses_amount)
def calculate_remaining_balance():
     remaining_balance = Monthly_Income - Monthly_Expenses
     remaining_balance = round(remaining_balance, 2)
     return(remaining_balance)
def calculate_savings_rate():
     savings_rate = ((Remaining_Balance / Monthly_Income) * 100)
     savings_rate = round(savings_rate, 2)
     return(savings_rate)
def determine_financial_status():
    if Monthly_Income > Monthly_Expenses:
        status = 'SAVING'
    elif Monthly_Expenses > Monthly_Income:
        status = 'OVERSPENDING'
    elif Monthly_Income == Monthly_Expenses:
         status = 'BREAKING EVEN'
    return(status)
           
Monthly_Income = calculate_monthly_income()
Monthly_Expenses = calculate_monthly_expenses()
Remaining_Balance = calculate_remaining_balance()
Savings_Rate = calculate_savings_rate()
Status = determine_financial_status()

print('Monthly Income is:', Monthly_Income, 'dollars')
print('Monthly Expenses is:', Monthly_Expenses, 'dollars') 
print('Remaining Balance is:', Remaining_Balance, 'dollars')
print('Savings Rate is:', Savings_Rate, "%")
print('Financial Status is:', Status)