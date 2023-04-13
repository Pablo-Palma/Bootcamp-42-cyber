cookbook = {
    "Sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10,
    },
    "Cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60,
    },
    "Salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15,
    },
}


def print_recipe(recipe_name):
    if recipe_name in cookbook:
        recipe = cookbook[recipe_name]
        print(f"Recipe for {recipe_name}:")
        print(f"Ingredients list: {recipe['ingredients']}")
        print(f"To be eaten for {recipe['meal']}.")
        print(f"Takes {recipe['prep_time']} minutes of cooking.")
    else:
        print(f"{recipe_name} is not in the cookbook.")


def delete_recipe(recipe_name):
    if recipe_name in cookbook:
        del cookbook[recipe_name]
        print(f"{recipe_name} has been deleted from the cookbook.")
    else:
        print(f"{recipe_name} is not in the cookbook.")


def add_recipe():
    recipe_name = input("Enter the recipe name: ")
    ingredients = input("Enter the ingredients separated by commas: ").split(",")
    meal = input("Enter the type of meal: ")
    prep_time = input("Enter the preparation time (in minutes): ")
    cookbook[recipe_name] = {"ingredients": ingredients, "meal": meal, "prep_time": prep_time}
    print(f"{recipe_name} has been added to the cookbook.")


def print_cookbook():
    print("Cookbook:")
    for recipe_name, recipe in cookbook.items():
        print_recipe(recipe_name)


def main():
    print("Welcome to the Python Cookbook !")
    while True:
        print(
            "List of available option:\n"
            "  1: Add a recipe\n"
            "  2: Delete a recipe\n"
            "  3: Print a recipe\n"
            "  4: Print the cookbook\n"
            "  5: Quit"
        )
        try:
            choice = int(input("Please select an option: "))
        except ValueError:
            print("Sorry, this option does not exist.")
            continue

        if choice == 1:
            add_recipe()
        elif choice == 2:
            recipe_name = input("Enter the recipe name: ")
            delete_recipe(recipe_name)
        elif choice == 3:
            recipe_name = input("Enter the recipe name: ")
            print_recipe(recipe_name)
        elif choice == 4:
            print_cookbook()
        elif choice == 5:
            print("Cookbook closed. Goodbye!")
            break
        else:
            print("Sorry, this option does not exist.")


if __name__ == "__main__":
    main()

