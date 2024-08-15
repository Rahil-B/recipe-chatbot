from query_handler import handle_question

def start_conversation(recipe):
    time_and_servings = recipe.get_time_and_servings()
    
    print(f"Let's start with the recipe for {recipe.title}.")
    print("Here are some details:")
    for label, value in time_and_servings.items():
        print(f"{label}: {value}")
    
    print("\nWhat would you like to do?")
    
    while True:
        user_input = input("\nYou can ask about ingredients, nutrition information, specific steps, or for help.\n")

        response = handle_question(user_input, recipe)

        if response == "ingredients":
            print("\nIngredients:")
            for ingredient in recipe.get_ingredients():
                print(f"- {ingredient}")
        elif response == "utensils":
            print("\nUtensils required:")
            for utensil in recipe.get_utensils():
                print(f"- {utensil}")
        elif "Nutrition Information:" in response:
            print(response)
        elif response == "steps":
            print(f"\nStep {recipe.current_step + 1}: {recipe.get_current_step()}")
        elif user_input.lower() in ['exit', 'quit', 'goodbye','bye']:
            print("Goodbye!")
        elif "For your query" in response:
            print(response)
        elif "Google Search" in response or "YouTube Search" in response:
            print(response)
        else:
            print(f"\n{response}")
