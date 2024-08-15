import streamlit as st
from recipe_parser import fetch_recipe
from recipe import Recipe
from query_handler import handle_question

# Define functions to display recipe details and handle user queries
def display_recipe_details(recipe):
    st.write(f"### Recipe: {recipe.title}")
    st.write(f"**Preparation Time and Servings:** ")
    for label, value in recipe.time_and_servings.items():
        st.write(f"- **{label}:** {value}")
    

def chat_with_user(recipe):
    st.write(f"### Chat with Recipe Bot")
    st.write(f"Example questions you can ask: 'What are the ingredients?', 'What utensils are required?', 'What is the next step?'")
    user_input = st.text_input("Ask about the recipe:")

    if user_input:
        response = handle_question(user_input, recipe)
        
        if response == "ingredients":
            st.write("**Ingredients:**")
            for ingredient in recipe.get_ingredients():
                st.write(f"- {ingredient}")
        elif response == "utensils":
            st.write("**Utensils Required:**")
            for utensil in recipe.get_utensils():
                st.write(f"- {utensil}")
        elif response == "steps":
            st.write(f"**Step {recipe.current_step + 1}:** {recipe.get_current_step()}")
        elif user_input.lower() in ['exit', 'quit', 'goodbye','bye']:
            st.write("Goodbye!")
        elif "For your query" in response:
            st.write(response)
        elif "Google Search" in response or "YouTube Search" in response:
            st.write(response)
        else:
            st.write(response)
        print(response)

# Main function for Streamlit app
def main():
    st.title("Recipe Chatbot")

    url = st.text_input("Please enter the recipe URL:")

    if url:
        try:
            recipe_data = fetch_recipe(url)
            recipe = Recipe(
                title=recipe_data['title'],
                ingredients=recipe_data['ingredients'],
                steps=recipe_data['steps'],
                time_and_servings=recipe_data['time_and_servings'],
                nutrition_info=recipe_data['nutrition_info'],
                utensils=recipe_data['utensils']
            )
            display_recipe_details(recipe)
            chat_with_user(recipe)
        except Exception as e:
            st.error(f"Error fetching recipe: {e}")

if __name__ == "__main__":
    main()
