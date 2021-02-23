from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy


def login(request):
    return render(request, "login.html")

def home(request):
    return render(request, "home.html")

def forgetPassword(request):
    return render(request, "forgetPassword.html")

def recipe(request):
    return render(request, "recipe.html")

def about(request):
    return render(request, "about.html")

def register(request):
    return render(request, "register.html")

def uploadHome(request):
    return render(request, "uploadHome.html")

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)

def editRecipeHome(request):
    return render(request, "editRecipeHome.html")

def parse_ingredient_file(recipe_arr):
    # ingredients_result = []
    # instructions_result = []
    ingredients_start = recipe_arr.index('Ingredients:\n')
    instructions_start = recipe_arr.index('Instructions:\n')
    ingredients_result = recipe_arr[ingredients_start + 1 : instructions_start]
    instructions_result = recipe_arr[instructions_start + 1 :]
    return ''.join(ingredients_result), ''.join(instructions_result)

def editRecipe(request):
    img_name = request.GET.get('img', 'shrimp')
    img = img_name + '.jpg'
    ingredient_file_path = request.GET.get('ingredient', 'honeygarlicshrimp')
    meal_name, ingredient_file = parse_txt('./media/' + ingredient_file_path + '.txt')
    ingredients, instructions = parse_ingredient_file(ingredient_file)
    result = { 'img_name': img_name, \
        'img': img, \
        'meal_name': meal_name, \
        'ingredient_file_path': ingredient_file_path, \
        'ingredients': ingredients, \
        'instructions': instructions }
    return render(request, 'editRecipe.html', result)
    
def parse_txt(txt_file_path):
    meal_name = ''
    result = []
    with open(txt_file_path) as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if i == 0:
                meal_name = line
            else:
                result.append(line)
    return meal_name, result

def viewRecipe(request):
    img_name = request.GET.get('img', 'shrimp')
    img = img_name + '.jpg'
    ingredient_file_path = request.GET.get('ingredient', 'honeygarlicshrimp')
    meal_name, ingredient_file = parse_txt('./media/' + ingredient_file_path + '.txt')
    result = { 'img_name': img_name, \
        'img': img, \
        'meal_name': meal_name, \
        'ingredient_file_path': ingredient_file_path, \
        'ingredient_file': ingredient_file }
    return render(request, "viewRecipe.html", result)