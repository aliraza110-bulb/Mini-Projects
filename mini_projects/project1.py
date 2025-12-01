# expense tracker
expenses=[]
def add_expenses():
    try:
         category=input("Enter Expenses : ").capitalize()
         amount=float(input("Enter The Amount Which You Spent : "))
         note=input("Enter The Short Note Or Discription : ")
         expense={
              "category":category,
              "amount":amount,
              "note":note

                   }
         expenses.append(expense)
         print("Expenses Added Successfully")
    except (ValueError):
         print("Invalid Input Please Input Valid Values")
    except Exception as e:
         print(f"An Expected Error{e}")

def view_expenses():
     try:
          if not expenses:
               print("No Record found")
               return
          for i,exp in enumerate(expenses,1):
               print(f"{i}.{exp['category']}-Rs.{exp['amount']} ({exp['note']}")
               total += exp['amount']
               print('\n')
               print('Total Expense',total)
     except Exception as e:
          print('Something Wrong ', e)

def search_by_category():
     try:
          cat=input("Enter Your Category : ")
          if not expenses:
               print('No record found')
               return
          found= [e for e in expenses if e["categotry"] == cat]
          if not found:
               print('No expenses found of this category')
               print(f"Rs{e['amount']} {e["note"]}")
     except Exception  as e:
          print("Some Thing Went Wrong",e)

def main():
     while True:
          print("WELCOME TO THE EXPENSES TRACKER")
          print("1.add expenses")
          print("2.view expenses")
          print("3.Search Expenses")
          
          choice =input("Enter Your Choice : ")
          if choice == "1":
            add_expenses()
          elif choice == "2":
            view_expenses()
          elif choice == '3':
            search_by_category()
          else:
              print("Invalid Input")


main()