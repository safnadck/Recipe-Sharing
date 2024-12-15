from django.shortcuts import render
from datetime import timedelta

# Homepage view
def homepage(request):
    return render(request, 'home.html')

# Recipe List View
def recipe_list(request):
    recipes = [
        {'id': 1, 'name': 'Pasta', 'prep_time': 15, 'category': 'Vegetarian'},
        {'id': 2, 'name': 'Chicken Curry', 'prep_time': 45, 'category': 'Non-Vegetarian'},
        {'id': 3, 'name': 'Chocolate Cake', 'prep_time': 90, 'category': 'Dessert'},
    ]
    return render(request, 'recipes.html', {'recipes': recipes})

# Recipe Details View
def recipe_details(request, recipe_id):
    recipes = [
        {'id': 1, 'name': 'Pasta', 'prep_time': 15, 'ingredients': ['Pasta', 'Tomato', 'Garlic'], 'instructions': 'Boil pasta, prepare sauce.'},
        {'id': 2, 'name': 'Chicken Curry', 'prep_time': 45, 'ingredients': ['Chicken', 'Curry Powder', 'Garlic'], 'instructions': 'Cook chicken, add spices.'},
        {'id': 3, 'name': 'Chocolate Cake', 'prep_time': 90, 'ingredients': ['Flour', 'Sugar', 'Cocoa Powder'], 'instructions': 'Mix ingredients, bake at 180°C for 30 minutes.'},
    ]
    recipe = next((r for r in recipes if r['id'] == recipe_id), None)
    return render(request, 'recipe_details.html', {'recipe': recipe})

# Category List View
def category_list(request):
    categories = [
        {'name': 'Vegetarian', 'recipes_count': 1},
        {'name': 'Non-Vegetarian', 'recipes_count': 1},
        {'name': 'Dessert', 'recipes_count': 1},
    ]
    return render(request, 'categories.html', {'categories': categories})

# Contact View
def contact(request):
    return render(request, 'contact.html')
