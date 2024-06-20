# Question 2: Double Scoop with Nested Loops

# Task 1: Your Mood Tracker

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
time_of_day = ["morning", "afternoon", "evening"]
my_mood = ["happy 😊!", "sad 😢.", "excited 🤩!", "mellow 😎.", "tired 😴.","festive 😺!", "passionate 😍."]

import random
for i in range(len(days_of_week)):
    for j in range(len(time_of_day)):
        day = days_of_week[i]
        time = time_of_day[j]
        mood = random.choice(my_mood)
        print(f"On {day} {time}, we were " + str(mood))