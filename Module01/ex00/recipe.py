class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type=None):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

        # Validar los valores de entrada
        if not isinstance(self.name, str):
            print("Error: el nombre debe ser una cadena de caracteres (str)")
            exit()
        if not isinstance(self.description, str):
            print("Error: la descripción debe ser una cadena de caracteres (str)")
            exit()
        if not isinstance(self.cooking_lvl, int) or self.cooking_lvl not in range(1, 6):
            print("Error: el nivel de dificultad de cocción debe ser un número entero entre 1 y 5")
            exit()
        if not isinstance(self.cooking_time, int) or self.cooking_time <= 0:
            print("Error: el tiempo de cocción debe ser un número entero positivo")
            exit()
        if not isinstance(self.ingredients, list):
            print("Error: los ingredientes deben ser una lista")
            exit()
        if self.recipe_type not in [None, "starter", "lunch", "dessert"]:
            print("Error: el tipo de receta debe ser 'starter', 'lunch' o 'dessert'")
            exit()

    def __str__(self):
        recipe_info = f"{self.name} ({self.recipe_type}): {self.description}\n"
        recipe_info += f"Nivel: {self.cooking_lvl} | Tiempo: {self.cooking_time} minutos\n"
        recipe_info += f"Ingredientes: {', '.join(self.ingredients)}"
        return recipe_info


# Ejemplo de uso
"""my_recipe = Recipe("Ensalada de frutas", 2, 10, ["fresas", "plátano", "uvas", "naranja"], "Una refrescante ensalada de frutas", "dessert")
print(my_recipe)"""
