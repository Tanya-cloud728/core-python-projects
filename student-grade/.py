
students={}
def add_stud():
 while True:
    name=input("enter student::")
    name=name.strip()
    name=name.title()
    if(name==""):
       print("name can't be empty")
       continue
    if name in students:
       print("student already exist")
       continue
    break
 while True:
  try:
    marks=int(input("enter marks::"))
    if(marks<0 or marks>100):
       print("enter valid marks bw 0 and 100")
       continue
    if(marks>=90):
       grade="A+"
    elif(marks>=80):
       grade="B"
    elif(marks>=70):
       grade="C"
    elif(marks>=60):
       grade="D"
    else:
       grade="F"
    break
  except ValueError:
    print("enter an integer::")
 students[name]={
        "marks":marks,
        "grade":grade
    } 
 print("student added successfully")
def view_stud(students):
 if not students:
   print("no stuents added yet::")
 else:
    for name,data in students.items():
      print("student","->",name)
      print("marks","->",data["marks"])
      print("grade","->",data["grade"])
      print("____________________")
      view_stud()
def search_stud(students):
   name=input("enter name to be search::")
   name=name.strip()
   name=name.title()
   if name in students:
      print(name,"->",students[name]["marks"],"--->",students[name]["grade"])
   else:
      print("student name doesnt exist")
def calculateAvg(students):
   if not  students:
      print("student doesnt exist")
   else:
    sum=0
    studentCnt=0
    for _,data in students.items():
     sum+=data["marks"]
     studentCnt+=1
    avg=sum/studentCnt
    print("average is::",avg)
def HighMark(students):
   if not students:
      print("student doesnt exist")
   else:
      Highest=-1
      for name,data in students.items():
         if(data["marks"]>Highest):
            Highest=data["marks"]
            student=name
      print("highest marks is::",student,"----->",Highest)
def DelStud(students):
   name=input("enter the student u want to delete:")
   name=name.strip()
   name=name.title()
   if name in students:
      del students[name]
      print("student deleted successfully:")
   else:
      print("student does,nt exist:")
def showMenu():
   print("1 -> Add student")
   print("2 -> View student")
   print("3 -> Calculate average")
   print("4 -> Highest marks")
   print("5 -> Delete student")
   print("6 -> Search student")
   print("7 -> Exit")
   choice=int(input("enter ur choice--->"))
   return choice
while True:
 try:
    choice=showMenu()
    if(choice==1):
       add_stud()
    elif(choice==2):
       view_stud()
    elif(choice==3):
       calculateAvg()
    elif(choice==4):
       HighMark()
    elif(choice==5):
       DelStud()
    elif(choice==6):
       search_stud()
    elif(choice==7):
       break
    else:
       print("invalid choice:;")
 except ValueError:
    print("enter valid choice::")
      
    
