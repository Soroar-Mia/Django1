from django.shortcuts import render

# Create your views here.

def index(request):
    meals = {'meals' : [
        {
            "strMeal": "BeaverTails",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ryppsv1511815505.jpg",
            "idMeal": "Facere placeat voluptates corporis veritatis vitae adipisci amet maiores aut a nisi porro modi eligendi sit quo libero cupiditate."
        },
        {
            "strMeal": "Breakfast Potatoes",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/1550441882.jpg",
            "idMeal": "Facere placeat voluptates corporis veritatis vitae adipisci amet maiores aut a nisi porro modi eligendi sit quo libero cupiditate."
        },
        {
            "strMeal": "Canadian Butter Tarts",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/wpputp1511812960.jpg",
            "idMeal": "Facere placeat voluptates corporis veritatis vitae adipisci amet maiores aut a nisi porro modi eligendi sit quo libero cupiditate."
        },
        {
            "strMeal": "Nanaimo Bars",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/vwuprt1511813703.jpg",
            "idMeal": "Facere placeat voluptates corporis veritatis vitae adipisci amet maiores aut a nisi porro modi eligendi sit quo libero cupiditate."
        },
        {
            "strMeal": "Pouding chomeur",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yqqqwu1511816912.jpg",
            "idMeal": "Facere placeat voluptates corporis veritatis vitae adipisci amet maiores aut a nisi porro modi eligendi sit quo libero cupiditate."
        },
        {
            "strMeal": "Poutine",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uuyrrx1487327597.jpg",
            "idMeal": "Facere placeat voluptates corporis veritatis vitae adipisci amet maiores aut a nisi porro modi eligendi sit quo libero cupiditate."
        },
        {
            "strMeal": "Rappie Pie",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ruwpww1511817242.jpg",
            "idMeal": "Facere placeat voluptates corporis veritatis vitae adipisci amet maiores aut a nisi porro modi eligendi sit quo libero cupiditate."
        },
        {
            "strMeal": "Split Pea Soup",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/xxtsvx1511814083.jpg",
            "idMeal": "Facere placeat voluptates corporis veritatis vitae adipisci amet maiores aut a nisi porro modi eligendi sit quo libero cupiditate."
        }
    ]}
    return render(request, 'index.html', meals)
