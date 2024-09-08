spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    foods=[food['name'] for food in spicy_foods]
    return (foods)

def get_spiciest_foods(spicy_foods):
    foods=[food  for food in spicy_foods if food['heat_level']>5]
    return(foods)     

def print_spicy_foods(spicy_foods):
    """Prints each food formatted with 🌶 emojis according to its heat level."""
    for food in spicy_foods:
        heat_emojis = '🌶' * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_emojis}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    return None  

     

def print_spiciest_foods(spicy_foods):
    """Prints foods with heat level over 5 formatted with 🌶 emojis."""
    spiciest_foods = get_spiciest_foods(spicy_foods)
    for food in spiciest_foods:
        heat_emojis = '🌶' * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_emojis}")
   


def get_average_heat_level(spicy_foods):
    
    heat_levels = [hot['heat_level'] for hot in spicy_foods]
    
    if heat_levels:
        average_heat_level = sum(heat_levels) / len(heat_levels)
    else:
        average_heat_level = 0
    
    return average_heat_level


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append( spicy_food)
    return spicy_foods


