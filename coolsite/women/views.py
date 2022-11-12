from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
# Импорт БД
from .models import  *

# title это то что написано на сылке
#menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]
menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
]

# Create your views here.
def index(request):
    # Это класс Women, получает все статти через ALL()
    posts = Women.objects.all()

    context = {
        'posts': posts,
        'title': 'Главная страница',
        'cat_selected': 0,
    }

    return render(request, 'women/index.html', context=context)

def about(request):
    return render(request, 'women/about.html', {'menu' : menu, 'title': 'О сайте'})

def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")

def show_category(request, cat_id):
    #выбираем с таблицы Women только те у которых   категория общая
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()
    context = {
        'posts': posts,
        'title': 'Отоброжение по рубрикам',
        'cat_selected': cat_id,
    }

    return render(request, 'women/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
