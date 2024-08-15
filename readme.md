# Recipe Chatbot

## Overview

The Recipe Chatbot is a Terminal based chat and  Streamlit-based application that allows users to interact with recipes through a chatbot interface. The chatbot can provide information about a recipe's ingredients, preparation steps, cooking utensils, and nutritional facts. Users can also navigate through the cooking steps, and if necessary, get external help through Google and YouTube search links.

## Features

- **Recipe Details**: View essential details such as preparation time, servings, ingredients, and nutrition information.
- **Interactive Chatbot**: Ask the chatbot about ingredients, utensils, nutrition facts, or specific cooking steps.
- **Step Navigation**: Navigate through cooking steps with commands like "next step", "previous step", and "repeat step".
- **External Help**: Get search links to Google or YouTube for further clarification or demonstration.

## Technologies Used

- **Python**
- **Streamlit**: For building the web interface.
- **Spacy**: For natural language processing to understand user queries.
- **Recipe Parser**: A custom parser to scrape recipe information from the web.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Rahil-B/recipe-chatbot.git
   cd recipe-chatbot
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python3 -m venv .venv
   source venv/bin/activate
   ```

3. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Download the Spacy English language model**:

   ```bash
   python -m spacy download en_core_web_sm
   ```

## Run Chatbot as terminal prompt or web app

**1. Run the Streamlit application**:

   ```bash
   python terminal_chatbor.py
   ```
**2. Run the Streamlit application**:

   ```bash
   streamlit run web_chatbot.py
   ```

2. **Enter a recipe URL** in the input field to load the recipe details. ( e.g. https://www.allrecipes.com/recipe/8408204/salami-ham-and-pepperoni-sandwiches-in-the-air-fryer/ )

3. **Interact with the chatbot** by typing questions or commands such as:
   - "What are the ingredients?"
   - "What utensils do I need?"
   - "Show me the nutrition facts."
   - "Next step" / "Previous step" / "Repeat step"
   - "How do I cook this?"

4. **Get external help**: If the chatbot can't find the information you're asking for, it will provide Google and YouTube search links.

## Project Structure

```bash
recipe-chatbot/
├── web_chatbot.py            # Main Streamlit app
├── recipe_parser.py          # Web scraping logic for extracting recipe details
├── terminal_chatbot.py       # Main terminal based chat app
├── conversation_helper.py    # Chatbot logic for processing user inputs and generating responses
├── recipe.py                 # Recipe class for storing and managing recipe data
├── query_handler.py          # Logic for handling user queries and chatbot responses
├── utensils.py               # Functions and classes for managing and retrieving utensil information
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## Future Improvements

- Add support for more complex queries and more recipe websites.
- Enhance the chatbot's understanding of conversational language.
- Include image or video content alongside recipe steps for better user guidance.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes.

## Acknowledgements

- Thanks to the developers of Streamlit and Spacy for the excellent tools that made this project possible.
- Recipe data is parsed from publicly available recipe websites.
