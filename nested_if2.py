# Question 2: Quick Decisions: The Event Planner 🎉

# Task 1: Code Correction

attendees = int(input("Enter number of attendees: "))
venue = "Large Hall" 
print(venue) if attendees > 100 else print("Conference Room")

# Task 2: Venue Selection

print("We offer an Audio System upgrade when using the Large Hall.") if attendees > 100 else print("We offer a Projector upgrade when using the Conference Room.")
upgrade = input("Would you like to upgrade your group's plan: (yes/no)? ")
print("Congradulations! You have chosen to enhance your group's plan with an upgrade!") if upgrade == "yes" else print("You have not selected an upgrade at this time.")

# Task 3: Catering Choices

meal_preference = input("What is your selection for your group's meal plan: (vegetarian or regular) gourmet? ")
print("Veggie Delight Caterers it is!") if meal_preference == "vegetarian" else print("Gourmet Meals Caterers it is!")