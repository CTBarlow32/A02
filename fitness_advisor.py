'''
Carter Barlow, IS 303, A02

Fitness Advisor
I am making a fitneess advisor that recommends an exercise plan based on
users fitness level and goals.


Input:
- Name (String)
-Fitness level (beginner, intermediate, advanced), (String)
-Fat loss goal (Integer)
-Muscle gain goal (Integer)


Processes:
-Validate fitness level is string and is either beginner, intermediate, or advanced
-Decide on exercise plan based on fitness level and goals

Output:
- Exercise plan based on fitness level and goals

'''

#Input
from ast import If


name = input("Enter your name: ")
fitness_level = input("Enter fitness level (beginner, intermediate, advanced): ").lower()
fat_loss_goal = int(input("Enter fat loss goal (in pounds): "))
muscle_gain_goal = int(input("Enter muscle gain goal (in pounds): "))

#Validate
fit_lev = ("beginner", "intermediate", "advanced")
if fitness_level not in fit_lev:
    print("Invalid fitness level, please input beginner, intermediate, or advanced.")

#Processes
if fitness_level == "advanced" and fat_loss_goal >10 and muscle_gain_goal >10:
    fitness_category = "your recommended exercise plan: 2-a days's, 4 times a week"

elif fitness_level == "intermediate" or fitness_level == "advanced" and fat_loss_goal > 5 and muscle_gain_goal > 5:
    fitness_category = "your recommended exercise plan: 1-a day, 4 times a week"

else:
    fitness_category = "your recommended exercise plan: 1-a day, 3 times a week"

print(f"Thank you {name} for using fitness advisor.\n"
      f"Based on your fitness level and goals, {fitness_category}.")