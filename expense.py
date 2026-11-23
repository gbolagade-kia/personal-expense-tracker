# •	Add an expense with date, description, category, and amount.
# •	View all recorded expenses in a readable format.
# •	Calculate total spending and totals for individual categories.
# •	Search or filter expenses by category or date.
# •	Save records to JSON or CSV so they remain after the program closes.
# •	Load\xisting records automatically when the program starts.
# •	Validate bad input, such as text entered where an amount is expected.

import csv
import math
import os
from datetime import date
today = date.today()

if os.path.exists('list.csv'):
    print("File present")
else:
    with open("list.csv", 'w') as fil:
        pass
size = os.path.getsize("list.csv")

if os.path.exists('settings.txt'):
    print("File present")
else:
    with open("settings.txt", 'w') as fil:
        pass
limitSize = os.path.getsize("settings.txt")

expenses = []

if limitSize == 0:
    while True:
        try:
            dailyLimit = int(input("How much do you set as your limit today?"))
            if dailyLimit > 0:
                break
            print("Number must be greater than 0")
        except ValueError:
            print("Please enter a valid whole number")
        
    
    with open("settings.txt",'w') as text:
        text.write(str(dailyLimit)) 

else:
    with open("settings.txt",'r') as text:
        dailyLimit = text.read()
    print(f"You have already set a daily limit")

             
print("Welcome to your expense Tracker")
while True:
    try:
        userExpense = int(input("How much did you spend today?"))
        if userExpense > 0:
            break
        print("Number must be greater than 0")
    except ValueError:
        print("Please enter a valid whole number")


expenseUse = input("What did you use the money for?")
category = input("Which category does it fall under?").strip().title()
 
print(f"Got it. You spent N{userExpense} on {expenseUse} today,{today}.")

expenseDict = {
    "Amount" : userExpense,
    "Purpose" : expenseUse,
    "Date" : today,
    "Category" : category
}
# expense.append(expenseDict)


with open('list.csv','a', newline= "") as file:
    csv_writer = csv.DictWriter(file,fieldnames = ["Amount", "Purpose", "Date", "Category"])

    if size == 0:
          csv_writer.writeheader()
          csv_writer.writerow(expenseDict)
    else:
        csv_writer.writerow(expenseDict) 

with open('list.csv', 'r') as f:
    csv_reader = csv.DictReader(f)
    for line in csv_reader:
         expenses.append(line)
Total = 0
for expense in expenses:
     if expense["Date"] == str(today):
         amount = int(expense['Amount'])
         Total += amount
         
     
print(f"Total is {Total}")
remaining = int(dailyLimit) - Total
print(f"The remaining amount left for you to spend today is {remaining}")

if dailyLimit != 0:
     percentageRemaining = (remaining/int(dailyLimit)) * 100
     print(f"You still have {percentageRemaining} %funds you can spend today")
     
barlength = 20
amountTobefilled = math.ceil((remaining / int(dailyLimit)) * 20)
emptySlots = barlength - amountTobefilled
amountPercent = (amountTobefilled/barlength) * 100

percentagebar = []

if Total <= int(dailyLimit):
    for i in range(amountTobefilled):
        percentagebar.append("🔋")
    for i in range(emptySlots):
            percentagebar.append("-")
    print('[' + "".join(percentagebar) + ']' + str(amountPercent) + '%')

else:
    print("You have exceeded your daily limit🙈")

for expense in expenses:
    print(f"Date : {expense['Date']}")
    print(f"Purpose : {expense['Purpose']}")
    print(f"Amount : ₦{expense['Amount']}")
    print(f"Category : {expense['Category']}")
    print("=================")

#Time to calculate category totals
categoryTotals = {}

for expense in expenses:
    category = expense["Category"]
    amount = int(expense["Amount"])

    if category in categoryTotals:
        categoryTotals[category] += amount
    else:
        categoryTotals[category] = amount

print("Category Totals")

for categora in categoryTotals:
    print(f'{categora} : N {categoryTotals[categora]}')


#search for expenses
wannaSearch = input("Do you wanna search for any Category of expenses?(Y/N)").strip().title()
if wannaSearch == 'Y':
    search = input("What Category do you want to search for?").strip().title()

    found = False
    for expense in expenses:
        category = expense["Category"]
        # print(search)
        # print(category)
        if search in category:
            found = True
            print(f"Date : {expense['Date']}")
            print(f"Purpose : {expense['Purpose']}")
            print(f"Amount : ₦{expense['Amount']}")
        
    if found == True:
        print("Found,above are the details of your searched category")
    if found == False:
        print("Couldn't find category") 

else:
    print('Okay☺👍')


#search by date
wannaSearchDate = input("Do you wanna search for any date of expenses?(Y/N)").strip().title()
if wannaSearchDate == 'Y':
    
    dateSearch = input("What date do you want to search for?")
    foundDate = False
    for expense in expenses:
        theDate = expense['Date']

        if dateSearch in theDate:
            foundDate = True
            print(f"Date : {expense['Date']}")
            print(f"Purpose : {expense['Purpose']}")
            print(f"Amount : ₦{expense['Amount']}")

    if foundDate == False:
        print("Couldn't find date")
    else:
        print("Found, here you go")
else:
    print("Okay, no problem")
    
     

       
    
