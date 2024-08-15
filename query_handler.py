import re
import spacy
nlp = spacy.load('en_core_web_sm')

def generate_search_links(query):
    search_query = "+".join(query.split())
    google_url = f"https://www.google.com/search?q={search_query}"
    youtube_url = f"https://www.youtube.com/results?search_query={search_query}"
    return google_url,youtube_url

def parse_query(query):
    doc = nlp(query.lower())
    print(doc.ents,query)
    # Check for step navigation commands first
    if re.search(r'\b(next|previous|repeat|prev)\b', query, re.I):
        if 'next' in query:
            return 'next_step'
        elif 'previous' in query or 'prev' in query:
            return 'previous_step'
        elif 'repeat' in query:
            return 'repeat_step'
    elif any(token.lemma_ in ['ingredient', 'ingredient list'] for token in doc):
        return 'ingredients'
    elif any(token.lemma_ in ['nutrition', 'calorie', 'fat', 'protein'] for token in doc):
        return 'nutrition_info'
    elif any(token.lemma_ in ['step', 'instruction'] for token in doc):
        step_number = next((int(ent.text) for ent in doc.ents if ent.label_ == 'ORDINAL'), None)
        return 'steps', step_number
    elif any(token.lemma_ in ['utensil','utensils', 'tool', 'equipment'] for token in doc):
        return 'utensils'
    elif any(token.lemma_ in ['how', 'what'] for token in doc):
        return 'how_to', query
    return 'help', query

def handle_question(query, recipe):
    intent = parse_query(query)

    if intent == 'ingredients':
        return "ingredients"
    elif intent == 'utensils':
        return "utensils"
    elif intent == 'nutrition_info':
        nutrition_info = recipe.get_nutrition_info()
        if nutrition_info:
            response = "\nNutrition Information:\n"
            for nutrient, value in nutrition_info.items():
                response += f"{nutrient}: {value}\n"
            return response
        else:
            return "No nutrition information available."
    elif intent[0] == 'steps':
        step_number = intent[1]
        if step_number:
            recipe.current_step = step_number - 1
        return "steps"
    elif intent == 'next_step':
        return recipe.next_step()
    elif intent == 'previous_step':
        return recipe.previous_step()
    elif intent == 'repeat_step':
        return recipe.get_current_step()
    elif intent[0] == 'how_to':
        google_url, youtube_url = generate_search_links(intent[1])
        return f"For your query, you can check: Google Search: {google_url} or YouTube Search: {youtube_url}"
    else:
        google_url, youtube_url = generate_search_links(intent[1])
        return f"Google Search: {google_url}\nYouTube Search: {youtube_url}"
