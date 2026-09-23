expense={}
def add_expense(expense):
    while True:
     name=input("enter expense::")
     if(name=={}):
        print("expense name cant be empty:")
        continue
     elif name in expense:
        print("name already exist")
        continue  
     else:
        break
     while True:
      try:
       amt=int(input("enter ammount::"))
       if(amt<=0):
          print("amount must be greater than 0")
          continue
       expense[name]=amt
       return expense
      except ValueError:     
       print("enter valid input::")    
def show_expense(expense):
    if not expense:
       print("no expense added yet!")
       return
    for name,amt in expense.items():
        print(name,"->",amt)
def del_exp(expense):
    dele=input("enter the name u want to delete::")
    if dele in expense:
     del expense[dele]
     return expense
    else:
        print("invalid name")
def total_expense(expense):
    if(expense=={}):
        print("no expense added yet!!")
    else:
     sum=0
     for i in expense.values():
        sum+=i
     print("your total expense is:",sum)
def Highest_exp(expense):
   if not expense:
      print("no expense added yet!")
      return
   max=0
   for name,items in expense.items():
      if(items>max):
         amount=name
         max=items
   print("your highest expense is::",name,"->",max)
def show(expense):
    choice=int(input("enter your choice:1->add expense,2->view,3->delete,4->total expense,5->highest expense,6->exit"))
    return choice
while True:
  try:
     choice=show(expense)
     if(choice==1):
        expense=add_expense(expense)    
     elif(choice==2):
        show_expense(expense)
     elif(choice==3):
        del_exp(expense)
     elif(choice==4):
         total_expense(expense)
     elif(choice==5):
        Highest_exp(expense)
     elif(choice==6):
      break
     else:
        print("invalid choice::")
  except ValueError:
       print("enter valid choice")

    







