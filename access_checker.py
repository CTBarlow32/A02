'''
Carter Barlow, IS 303, A02
Access Checker
I am making a access checker to determine if a user has access to
a website based on positon in company and day of the week.

Inputs:
- Name (string)
- Position in company (admin, employee, visitor) (string)
- Day of the week (string)

Processes:
- Validate position in company
- If manager, give passcode to enter admin section
- Check if user has access to website based on position and day of week

Outputs:
- If user has access to website or not
'''

#Input

name = input("Enter your name: ")
position = input("Enter position in company (admin, employee, visitor): ").lower()
day_of_week = input("Enter day of the week: ").lower()

#Validate

if position not in ["admin", "employee", "visitor"]:
    print("Invalid position, please input Admin, Employee, or Visitor.")

if position == "admin":
    admin_password = input("What is the admin password?")
    if admin_password != "hi_professor_giboney":
        print("Incorrect password, fool!!!")
    if admin_password == "hi_professor_giboney":
        access_status = "You have access to all sections of website."


#Processes
elif position == "employee" and day_of_week in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    access_status = "You have access to sections 1-5 of website."
elif position == "employee" and day_of_week in ["saturday", "sunday"]:
    access_status = "Bro go home, it's the weekend!!!"

elif position == "visitor" and day_of_week in ["saturday", "sunday"]:
    access_status = "You have access to sections 1-2 of website."

elif position == "visitor" and day_of_week in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    access_status = "Get out of here, go back to your normal job!"

#Output
print(f"Welcome {name}!\n"
      f"Based on your position and day of the week, {access_status}\n"
      f"Have a good day!")


