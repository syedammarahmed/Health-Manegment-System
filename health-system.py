#HEALTH MANEGMENT SYSTEM
print("Your code for your File is with your name\n"
      "Ammar : 1\n"
      "Qanet : 2\n"
      "Umar  : 3")
user_name = int(input("Please Enter your code  :  "))
print("\ncode for choice\n"
      "food : 1\n"
      "Gym  : 2")
user_choice = int(input("Please enter your choice code : "))
#Using if else or elif for condition on choice or name
if user_name==1 and user_choice==1:
      with open("Ammar1.txt","w") as f:
            #This def function created for to print current and date and time as par Internet
            def getdate():
                  import datetime
                  return datetime.datetime.now()
            print("Todays date and time is ","[", getdate(), "]")
            a=f.write(input("Enter you todays food routine : "))
elif user_name==1 and user_choice==2:
      with open("Ammar2.txt", "w") as f:
            def getdate():
                  import datetime
                  return datetime.datetime.now()
            print("Todays date and time is ", "[", getdate(), "]")
            a = f.write(input("Enter you todays Gym routine : "))
elif user_name==2 and user_choice==1:
      with open("Qanet1.txt", "w") as f:
            def getdate():
                  import datetime
                  return datetime.datetime.now()
            print("Todays date and time is ", "[", getdate(), "]")
            a = f.write(input("Enter you todays Food routine : "))
elif user_name==2 and user_choice==2:
      with open("Qanet2.txt", "w") as f:
            def getdate():
                  import datetime
                  return datetime.datetime.now()
            print("Todays date and time is ", "[", getdate(), "]")
            a = f.write(input("Enter you todays Gym routine : "))
elif user_name==3 and user_choice==1:
      with open("Umar1.txt", "w") as f:
            def getdate():
                  import datetime
                  return datetime.datetime.now()
            print("Todays date and time is ", "[", getdate(), "]")
            a = f.write(input("Enter you todays Food routine : "))
elif user_name==3 and user_choice==2:
      with open("Umar2.txt", "w") as f:
            def getdate():
                  import datetime
                  return datetime.datetime.now()
            print("Todays date and time is ", "[", getdate(), "]")
            a = f.write(input("Enter you todays Gym routine : "))
elif user_name>=3 and user_choice>=2:
      print("ERROR\n"
            "Please check Re-check Your Code Number\n")
print("Select Yes or NO\n"
      "Yes for close\n"
      "No  for retrieve")
user_final= input("Enter Yes or No : ").capitalize()
#Using while loop to stop as par condition
while(user_final=="Yes"):
      if user_final=="Yes":
            print("Great u have Successfully safe your File")
            break
while(user_final=="No"):
      print("\nChoose code for which file u want to retrieve\n"
      "Food : 1\n"
      "Gym  : 2")
      user_code= int(input("Enter your code : "))
      if user_name== 1 and user_final=="No" and user_code==1:
            print("\nYour previous data is : ")
            print("[",getdate(),"]")
            file= open("Ammar1.txt")
            content = file.read()
            print(content)
            with open("Ammar1.txt", "a") as f:
                  a = f.write(input("\nEnter your New text : "))
      elif user_name==1 and user_final=="No" and user_code==2:
            print("\nYour previous data is : ")
            print("[",getdate(),"]")
            file= open("Ammar2.txt")
            content = file.read()
            print(content)
            with open("Ammar2.txt", "a") as f:
                  a = f.write(input("\nEnter your New text : "))
      elif user_name==2 and user_final=="No" and user_code==1:
            print("\nYour previous data is : ")
            print("[",getdate(),"]")
            file= open("Qanet1.txt")
            content = file.read()
            print(content)
            with open("Qanet1.txt", "a") as f:
                  a = f.write(input("\nEnter your New text : "))
      elif user_name==2 and user_final=="No" and user_code==2:
            print("\nYour previous data is : ")
            print("[",getdate(),"]")
            file= open("Qanet2.txt")
            content = file.read()
            print(content)
            with open("Qanet2.txt", "a") as f:
                  a = f.write(input("\nEnter your New text : "))
      elif user_name==3 and user_final=="No" and user_code==1:
            print("\nYour previous data is : ")
            print("[",getdate(),"]")
            file= open("Umar1.txt")
            content = file.read()
            print(content)
            with open("Umar1.txt", "a") as f:
                  a = f.write(input("\nEnter your New text : "))
      elif user_name==3 and user_final=="No" and user_code==2:
            print("\nYour previous data is : ")
            print("[",getdate(),"]")
            file= open("Umar2.txt")
            content = file.read()
            print(content)
            with open("Umar2.txt", "a") as f:
                  a = f.write(input("\nEnter your New text : "))
      print("Your Data is successfully safe")
      break