import requests
from bs4 import BeautifulSoup
from utensils import extract_utensils_nlp

def fetch_recipe(url):
    
    response = requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://www.google.com',
    })
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the recipe. Status code: {response.status_code}")
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract recipe title
    title = soup.find('h1', class_='article-heading type--lion').text.strip()
    
    # Extract ingredients
    ingredients = []
    for ingredient in soup.find_all('li', class_='mm-recipes-structured-ingredients__list-item'):
        ingredients.append(ingredient.text.strip())
    
    # Extract steps
    steps = []  
    for step in soup.find_all('li', class_='comp mntl-sc-block mntl-sc-block-startgroup mntl-sc-block-group--LI'):
        step_text = step.find('p').text.strip()
        steps.append(step_text)
    
    # Extract utensils from steps
    utensils = extract_utensils_nlp(steps)
    
    # Extract time and servings information
    time_and_servings = {}
    for item in soup.find_all('div', class_='mm-recipes-details__item'):
        label = item.find('div', class_='mm-recipes-details__label').text.strip()
        value = item.find('div', class_='mm-recipes-details__value').text.strip()
        time_and_servings[label] = value
    
    # Extract nutrition information
    nutrition_info = {}
    nutrition_table = soup.find('table', class_='mm-recipes-nutrition-facts-label__table')
    if nutrition_table:
        rows = nutrition_table.find_all('tr')
        for row in rows:
            columns = row.find_all('td')
            if len(columns) == 2:
                nutrient_name = columns[0].text.strip()
                nutrient_value = columns[1].text.strip()
                nutrition_info[nutrient_name] = nutrient_value

    return {
        "title": title,
        "ingredients": ingredients,
        "steps": steps,
        "time_and_servings": time_and_servings,
        "nutrition_info": nutrition_info , # Include the nutrition information
        "utensils": utensils
    }

