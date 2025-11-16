# Project: Daily Calorie Tracker
# Name: Yuvraj singh
# Date: 16/11/2025
# Title: Daily Calorie Tracker CLI

import datetime

print("\nWelcome to the Daily Calorie Tracker CLI!")
print("Log your meals, track your calories, and manage your daily goals.\n")

# Data Collection
meal_names = []
calorie_amounts = []
meal_count = int(input("How many meals do you want to enter? "))

for i in range(meal_count):
    meal = input(f"Enter meal {i+1} name: ")
    calories = float(input(f"Enter calories for {meal}: "))
    meal_names.append(meal)
    calorie_amounts.append(calories)

# Calculations
total_calories = sum(calorie_amounts)
average_calories = total_calories / meal_count
daily_limit = float(input("Enter your daily calorie limit: "))

# Warning or Success Message
if total_calories > daily_limit:
    status_msg = f"Warning: You have exceeded your daily limit by {total_calories - daily_limit} calories!"
else:
    status_msg = "Success: You stayed within your daily calorie limit!"

# Summary Table
print("\nMeal Name\tCalories")
print("-" * 30)
for meal, cal in zip(meal_names, calorie_amounts):
    print(f"{meal}\t\t{cal}")
print("-" * 30)
print(f"Total\t\t{total_calories}")
print(f"Average\t\t{average_calories:.2f}")
print(status_msg)

# Bonus: Save to File
save_log = input("\nDo you want to save this session? (y/n): ").lower()
if save_log == 'y':
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("calorielog.txt", "w") as file:
        file.write(f"Session Time: {now}\n")
        file.write("Meal Name\tCalories\n")
        for meal, cal in zip(meal_names, calorie_amounts):
            file.write(f"{meal}\t\t{cal}\n")
        file.write(f"Total\t\t{total_calories}\n")
        file.write(f"Average\t\t{average_calories:.2f}\n")
        file.write(status_msg + "\n")
    print("Session saved to calorielog.txt")

# End of program
