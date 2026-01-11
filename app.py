from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)



recipes = {
    "Vegetable Biryani": {
        "ingredients": ["rice", "mixed vegetables", "onions", "spices", "coconut milk"],
        "steps": ["Sauté onions and spices.", "Add vegetables and rice.", "Cook with coconut milk."],
      
        "dietary": ["vegan", "gluten-free"]
    },
    "Dal Tadka": {
        "ingredients": ["lentils", "tomatoes", "onions", "spices", "oil"],
        "steps": ["Cook lentils.", "Sauté onions, tomatoes, and spices.", "Mix and garnish."],
       
        "dietary": ["vegan", "gluten-free"]
    },
    "Baingan Bharta": {
        "ingredients": ["eggplant", "tomatoes", "onions", "spices", "oil"],
        "steps": ["Roast eggplant.", "Sauté onions and spices.", "Mash and mix with tomatoes."],
       
        "dietary": ["vegan", "gluten-free"]
    },
    "Vegetable Korma": {
        "ingredients": ["mixed vegetables", "coconut milk", "spices", "onions", "nuts"],
        "steps": ["Sauté onions and spices.", "Add vegetables and coconut milk.", "Simmer and garnish with nuts."],
        
        "dietary": ["vegan", "gluten-free"]
    },
    "Poha": {
        "ingredients": ["flattened rice", "potatoes", "onions", "spices", "oil"],
        "steps": ["Sauté onions and spices.", "Add potatoes and poha.", "Cook until fluffy."],
        
        "dietary": ["vegan", "gluten-free"]
    },
    "Chana Masala": {
        "ingredients": ["chickpeas", "tomatoes", "onions", "spices", "garam masala"],
        "steps": ["Sauté onions and spices.", "Add tomatoes and chickpeas.", "Simmer and season."],
       
        "dietary": ["vegan", "gluten-free"]
    },
    "Aloo Gobi": {
        "ingredients": ["potatoes", "cauliflower", "onions", "spices", "oil"],
        "steps": ["Sauté onions and spices.", "Add potatoes and cauliflower.", "Cook until tender."],
       
        "dietary": ["vegan", "gluten-free"]
    },
    "Masala Dosa": {
        "ingredients": ["rice", "lentils", "potatoes", "spices", "oil"],
        "steps": ["Ferment rice-lentil batter.", "Cook potato filling.", "Make dosa and stuff."],
       
        "dietary": ["vegan", "gluten-free"]
    },
    "Rajma": {
        "ingredients": ["kidney beans", "tomatoes", "onions", "spices", "rice"],
        "steps": ["Soak and cook beans.", "Sauté onions and spices.", "Mix and simmer."],
       
        "dietary": ["vegan", "gluten-free"]
    },
    "Palak Tofu": {
        "ingredients": ["spinach", "tofu", "onions", "spices", "oil"],
        "steps": ["Sauté onions and spices.", "Add spinach and tofu.", "Cook until blended."],
       
        "dietary": ["vegan", "gluten-free"]
    },
    "Mutter Tofu": {
        "ingredients": ["peas", "tofu", "tomatoes", "spices", "cream substitute"],
        "steps": ["Sauté spices and tomatoes.", "Add peas and tofu.", "Simmer with cream substitute."],
       
        "dietary": ["vegan", "gluten-free"]
    },
    "Bhindi Masala": {
        "ingredients": ["okra", "onions", "spices", "tomatoes", "oil"],
        "steps": ["Sauté onions and spices.", "Add okra and tomatoes.", "Cook until tender."],
       
        "dietary": ["vegan", "gluten-free"]
    },
    "Kadai Vegetables": {
        "ingredients": ["mixed vegetables", "bell peppers", "spices", "onions", "oil"],
        "steps": ["Sauté onions and spices.", "Add vegetables and peppers.", "Stir-fry and season."],
       
        "dietary": ["vegan", "gluten-free"]
    },
    "Vegetable Pulao": {
        "ingredients": ["rice", "vegetables", "spices", "onions", "nuts"],
        "steps": ["Sauté onions and spices.", "Add rice and vegetables.", "Cook and garnish with nuts."],
      
        "dietary": ["vegan", "gluten-free"]
    },
    "Coconut Curry": {
        "ingredients": ["coconut milk", "vegetables", "spices", "onions", "curry leaves"],
        "steps": ["Sauté onions and spices.", "Add coconut milk and vegetables.", "Simmer."],
        
        "dietary": ["vegan", "gluten-free"]
    },
    "Lentil Soup": {
        "ingredients": ["lentils", "vegetables", "spices", "onions", "broth"],
        "steps": ["Sauté onions and spices.", "Add lentils and vegetables.", "Simmer in broth."],
        "image": "https://example.com/lentilsoup.jpg",
        "dietary": ["vegan", "gluten-free"]
    },
    "Stuffed Bell Peppers": {
        "ingredients": ["bell peppers", "rice", "spices", "onions", "nuts"],
        "steps": ["Mix filling with rice and spices.", "Stuff peppers.", "Bake or steam."],
        
        "dietary": ["vegan", "gluten-free"]
    },
    "Eggplant Curry": {
        "ingredients": ["eggplant", "coconut milk", "spices", "onions", "oil"],
        "steps": ["Sauté onions and spices.", "Add eggplant and coconut milk.", "Cook."],
       
        "dietary": ["vegan", "gluten-free"]
    },
    "Potato Curry": {
        "ingredients": ["potatoes", "tomatoes", "spices", "onions", "oil"],
        "steps": ["Sauté onions and spices.", "Add potatoes and tomatoes.", "Simmer."],
        
        "dietary": ["vegan", "gluten-free"]
    },
    "Chickpea Curry": {
        "ingredients": ["chickpeas", "coconut milk", "spices", "onions", "spinach"],
        "steps": ["Sauté onions and spices.", "Add chickpeas and coconut milk.", "Mix with spinach."],
        
        "dietary": ["vegan", "gluten-free"]
    }
}
  
    
      
    



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/roulette', methods=['POST'])
def roulette():
    # Get user inputs
    ingredients = [i.strip().lower() for i in request.form.get('ingredients', '').split(',') if i.strip()]
    dietary = request.form.getlist('dietary')  # e.g., ['vegan', 'gluten-free']
    
    # Filter recipes: Must contain all input ingredients and match dietary filters
    matching_recipes = []
    for name, data in recipes.items():
        recipe_ings = [i.lower() for i in data['ingredients']]
        if all(ing in recipe_ings for ing in ingredients):  # All ingredients present
            if all(tag in data['dietary'] for tag in dietary):  # All dietary tags match
                matching_recipes.append((name, data))
    
    if not matching_recipes:
        return render_template('recipe.html', recipe=None, message="No Indian recipes match your ingredients and filters!")
    
    # Randomly select one
    selected = random.choice(matching_recipes)
    return render_template('recipe.html', recipe=selected[1], name=selected[0])

if __name__ == '__main__':
    app.run(debug=True)