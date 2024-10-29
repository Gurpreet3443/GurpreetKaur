import tkinter as tk
from tkinter import messagebox, simpledialog

# Pre-loaded recipes with ingredients
recipes = {
    "pancakes": ["flour", "eggs", "milk", "butter", "sugar", "baking powder"],
    "spaghetti bolognese": ["spaghetti", "ground beef", "tomato sauce", "onion", "garlic", "olive oil"],
    "omelette": ["eggs", "milk", "salt", "pepper", "cheese"],
    "salad": ["lettuce", "tomato", "cucumber", "olive oil", "salt", "pepper"],
}

# Store user's pantry as a set of available ingredients
pantry = set()

# Function to add a new recipe
def add_recipe():
    recipe_name = simpledialog.askstring("Add Recipe", "Enter the recipe name:")
    if recipe_name:
        ingredients = simpledialog.askstring("Add Recipe", "Enter ingredients (comma-separated):")
        if ingredients:
            ingredients_list = [ingredient.strip().lower() for ingredient in ingredients.split(',')]
            recipes[recipe_name.lower()] = ingredients_list
            messagebox.showinfo("Success", f"Recipe for '{recipe_name}' added successfully.")

# Function to view all recipes
def view_recipes():
    if not recipes:
        messagebox.showinfo("Recipes", "No recipes added yet.")
        return
    recipes_list = "\n".join([f"- {recipe.title()}: {', '.join(ingredients)}" for recipe, ingredients in recipes.items()])
    messagebox.showinfo("Recipes", f"Recipes:\n{recipes_list}")

# Function to add ingredients to pantry
def add_to_pantry():
    new_ingredients = simpledialog.askstring("Add to Pantry", "Enter ingredients to add to your pantry (comma-separated):")
    if new_ingredients:
        new_ingredients_list = [ingredient.strip().lower() for ingredient in new_ingredients.split(',')]
        pantry.update(new_ingredients_list)
        messagebox.showinfo("Success", f"Ingredients '{', '.join(new_ingredients_list)}' added to pantry.")

# Function to check if a recipe can be made
def check_recipe():
    recipe_name = simpledialog.askstring("Check Recipe", "Enter the name of the recipe you want to check:")
    if recipe_name:
        recipe_name = recipe_name.lower()
        if recipe_name not in recipes:
            messagebox.showerror("Error", f"No recipe found with the name '{recipe_name}'.")
            return
        recipe_ingredients = set(recipes[recipe_name])
        missing_ingredients = recipe_ingredients - pantry
        if not missing_ingredients:
            messagebox.showinfo("Success", f"You have all the ingredients to make '{recipe_name.title()}'.")
        else:
            messagebox.showinfo("Missing Ingredients", f"You're missing these ingredients to make '{recipe_name.title()}': {', '.join(missing_ingredients)}")

# Function to view pantry contents
def view_pantry():
    if not pantry:
        messagebox.showinfo("Pantry", "Your pantry is empty.")
    else:
        messagebox.showinfo("Pantry", f"Your pantry contains: {', '.join(pantry)}")

# Main function to run the recipe book
def recipe_book():
    root = tk.Tk()
    root.title("Recipe Book")

    # Create buttons for each functionality
    btn_add_recipe = tk.Button(root, text="Add a Recipe", command=add_recipe)
    btn_view_recipes = tk.Button(root, text="View All Recipes", command=view_recipes)
    btn_add_to_pantry = tk.Button(root, text="Add Ingredients to Pantry", command=add_to_pantry)
    btn_view_pantry = tk.Button(root, text="View Pantry", command=view_pantry)
    btn_check_recipe = tk.Button(root, text="Check if You Can Make a Recipe", command=check_recipe)
    btn_exit = tk.Button(root, text="Exit", command=root.quit)

    # Arrange buttons in the window
    btn_add_recipe.pack(pady=10)
    btn_view_recipes.pack(pady=10)
    btn_add_to_pantry.pack(pady=10)
    btn_view_pantry.pack(pady=10)
    btn_check_recipe.pack(pady=10)
    btn_exit.pack(pady=20)

    root.mainloop()

# Run the recipe book app
if __name__ == "__main__":
    recipe_book()


