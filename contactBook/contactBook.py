contacts={}
choice=int(input("enter your choice:: 1 → Add Contact,2 → Search Contact,3 → Delete Contact,4 → View Contacts,5 :→ Exit--->"))
while choice!=5:
 if(choice==1):
    name=input("enter your name::")
    phone=input("enter yur phone::")
    contacts[name]=phone
 if(choice==2):
     name=input("enter the name you want to search")
     if(name in contacts):
         print(contacts[name])
     else:
         print("contact does'nt exist")
 if(choice==3):
    name=input("enter the name you want to delete")
    if(name is contacts):
        del contacts[name]
    else:
        print("contact does'nt exist")
 if(choice==4):
    for name,phone in contacts.items():
        print(name,"->",phone)
 choice=int(input("enter your choice:: 1 → Add Contact,2 → Search Contact,3 → Delete Contact,4 → View Contacts,5 :→ Exit"))

    

