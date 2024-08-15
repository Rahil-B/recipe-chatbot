class Recipe:
    def __init__(self, title, ingredients, steps, time_and_servings, nutrition_info,utensils):
        self.title = title
        self.ingredients = ingredients
        self.steps = steps
        self.current_step = 0
        self.time_and_servings = time_and_servings
        self.nutrition_info = nutrition_info  # Store the nutrition information
        self.utensils = utensils 

    def get_ingredients(self):
        return self.ingredients
    
    def get_time_and_servings(self):
        return self.time_and_servings
    
    def get_nutrition_info(self):
        return self.nutrition_info  # Method to access nutrition info
    
    def get_current_step(self):
        return self.steps[self.current_step]
    
    def next_step(self):
        if self.current_step < len(self.steps) - 1:
            self.current_step += 1
        return self.get_current_step()
    
    def previous_step(self):
        if self.current_step > 0:
            self.current_step -= 1
        return self.get_current_step()
    
    def get_utensils(self):
        return self.utensils
    
    # #Debugging
    # def __str__(self) -> str:
    #     print(self.steps, self.current_step,self.next_step(),self.previous_step())
