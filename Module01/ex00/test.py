from recipe import Recipe
from book import Book

# Creamos una instancia de Book
my_book = Book("My Cookbook")

# Creamos algunas recetas
recipe1 = Recipe("Spaghetti Carbonara", 3, 30, ["pasta", "eggs", "bacon", "parmesan cheese"], "Classic Italian pasta dish", "starter")
recipe2 = Recipe("Cheeseburger", 2, 20, ["ground beef", "cheddar cheese", "lettuce", "tomato", "bun"], "All-American burger", "lunch")
recipe3 = Recipe("Chocolate Cake", 4, 60, ["flour", "sugar", "cocoa powder", "eggs", "butter", "milk"], "Decadent dessert for chocolate lovers", "dessert")

# Añadimos las recetas al libro de recetas
my_book.add_recipe(recipe1)
my_book.add_recipe(recipe2)
my_book.add_recipe(recipe3)

""""# Buscamos una receta por nombre
my_book.get_recipe_by_name("Cheeseburger")"""

# Obtenemos todas las recetas de un tipo
my_book.get_recipes_by_types("starter")

