# Question 1: Nested Decisions: The Adventure Game 🏰

# Task 1: Code Correction

place = input("Choose a place: (forest or cave)? ")

if place == "forest":
    action = input("Choose an action: (climb a tree or cross a river)? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")


# Task 2: Setting the Scene

elif place == "cave":
    print("You found a hidden treasure!")
    cave_action = input("Do you want to: (light a torch or proceed in the dark)? ")
    if cave_action == "light a torch":
        print("You see a slime pit in front of you, and a cave exit to your right. Proceed right and exit this cave with your treasure in tact! 💰💰💰")
    elif cave_action == "proceed in the dark":
        print("Oh no! You and your treasure have fallen into a slime pit! 😫")

# Task 3: Default Path

else:
    # print("You have lost the game. 😱")
    pass # Will finish this later.