from datetime import datetime
from recipe import Recipe


class Book:
    def __init__(self, name):
        self.name = name
        self.creation_date = datetime.now()
        self.last_update = datetime.now()
        self.recipes_list = {"starter": [], "lunch": [], "dessert": []}

    def get_recipe_by_name(self, name):
        for recipe_type in self.recipes_list:
            for recipe in self.recipes_list[recipe_type]:
                if recipe.name == name:
                    print(recipe)
                    return recipe
        print(f"No recipe found with the name '{name}'")
        return None

    def get_recipes_by_types(self, recipe_type):
        if recipe_type not in self.recipes_list:
            print(f"No recipes found for the type '{recipe_type}'")
            return []
        recipes = self.recipes_list[recipe_type]
        for recipe in recipes:
            print(recipe.name)
        return recipes

    def add_recipe(self, recipe):
        if not isinstance(recipe, Recipe):
            print("Error: argument is not an instance of Recipe")
            return
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()

