# Question 1: Encapsulation in Personal Budget Management

# Task 1: Define Budget Category Class

from termcolor import colored


categories = {}
class BudgetCategory:
    # Constructor and private attributes
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget


# Task 2: Implement Getters and Setters

    # Getters and setters for category name and budget
    def get_category_name(self):
        return self.__category_name
    
    def set_category_name(self, new_category_name):
        self.__category_name = new_category_name

    def get_allocated_budget(self):
        return self.__allocated_budget
    
    def set_allocated_budget(self, new_allocated_budget):
        if new_allocated_budget > 0:
            self.__allocated_budget = new_allocated_budget


# Task 3: Add Budget Functionality

    def add_expense(self, category_name):
        # Method to add an expense to the category
        amount = int(input("Enter expense amount: "))
        if 0 < amount <= self.get_allocated_budget():
            self.set_allocated_budget(self.get_allocated_budget() - amount)
            return f"Category: {category_name} Expense: ${amount} Remaining Budget: ${self.get_allocated_budget()}"
        else:
             print("Invalid expense amount or insufficient budget balance.")

# Task 4: Display Budget Details

    def display_category_summary(self):
        # Method to display the budget category details
        print(colored(f"\nBudget Details", "white", attrs=["bold"]))
        print(colored(f"Budget Category: {self.get_category_name()} \nRemaining Budget: ${self.get_allocated_budget()}", "grey"))

# Function to get user input for category name and budget
def add_category(categories):
    category_name = input("Enter category name: ").title()
    allocated_budget = int(input("Enter budget for this category: "))
    categories[category_name] = BudgetCategory(category_name, allocated_budget)

# Main function to implement the desired choice of the user
def main():
    while True:
        print("\n1. Add Category\n2. Add Expense\n3. Display Details\n4. Exit")
        choice = input("Enter your choice: ")
        try:
            if choice == "1":
                add_category(categories)
            elif choice == "2":
                for category in categories:
                    print(f"Category: {category}")
                category_name = input("Enter category of expense: ").title()
                categories[category_name].add_expense(category_name)
            elif choice == "3":
                for category in categories.values():
                    category.display_category_summary()
            elif choice == "4":
                print("\n👋 Goodbye 👋\n")
                break
            else:
                print("Invalid entry, please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()