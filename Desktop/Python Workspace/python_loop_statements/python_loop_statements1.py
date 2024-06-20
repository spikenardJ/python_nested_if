# Question 1: The Range Riddle

# Task 1: Your Mood Today

days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
moods = ["happy 😊!", "sad 😢.", "energetic 🤩!", "calm 😎."]

import random
for i in range(len(days_of_the_week)):
    day = days_of_the_week[i]
    mood = random.choice(moods)
    print(f"On {day}, we were feeling " + str(mood))

