import spacy

# Load the NLP model
nlp = spacy.load("en_core_web_sm")

COMMON_UTENSILS = ["pan","saucepan", "bowl", "whisk", "grater", "knife", "spatula", "baking sheet", "pot", "skillet","spoon","fork","tongs","ladle","rolling pin","measuring cup","measuring spoon","colander","microwave","air fryer","fryer"]

def extract_utensils_nlp(steps):
    utensils_found = set()
    for step in steps:
        doc = nlp(step.lower())
        for token in doc:
            if token.pos_ == 'NOUN' and token.text in COMMON_UTENSILS:
                utensils_found.add(token.text)
        
    return list(utensils_found)
