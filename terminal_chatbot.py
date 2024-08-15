from recipe_parser import fetch_recipe
from recipe import Recipe
from conversation_helper import start_conversation

def main():
    url = input("Please enter the recipe URL: ")
    recipe_data = fetch_recipe(url)
    
    time_and_servings = recipe_data['time_and_servings']
    nutrition_info = recipe_data['nutrition_info']
    
    recipe = Recipe(
        recipe_data['title'], 
        recipe_data['ingredients'], 
        recipe_data['steps'], 
        time_and_servings,
        nutrition_info,
        utensils=recipe_data['utensils']
    )

    start_conversation(recipe)

if __name__ == "__main__":
    main()
