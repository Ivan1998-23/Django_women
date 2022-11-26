from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
# Импорт БД
from .models import *
from .utils import *


# title это то что написано на сылке
#menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


class WomenHome(DataMixin, ListView):
    paginate_by = 2
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Головна сторінка')
        return dict(list(context.items()) + list(c_def.items()))


    def get_queryset(self):
        return Women.objects.filter(is_published=True)

# Create your views here.
# def index(request):
#     # Это класс Women, получает все статти через ALL()
#     posts = Women.objects.all()
#
#     context = {
#         'posts': posts,
#         'title': 'Главная страница',
#         'cat_selected': 0,
#     }
#     return render(request, 'women/index.html', context=context)

def about(request):
    contact_list = Women.objects.all()
    paginator = Paginator(contact_list, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'women/about.html', {'page_obj': page_obj, 'menu' : menu, 'title': 'О сайте'})
#
class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    # генерация ошибки "Доступ запрещон"  403 Forbidden
    # raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return dict(list(context.items()) + list(c_def.items()))



# def addpage(request):
#     #Проверка на то что пользователь ввел не правильные данные
#     #Если нажмет отправить но дынные не правильные то он вернет страницу с правильными
#     # строками
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             try:
#                 form.save()
#                 return redirect('home')
#             except:
#                 form.add_error(None, 'Ошибка добавления поста')
#
#     else:
#         form = AddPostForm()
#     return render(request, 'women/addpage.html', {'form': form,  'memu': menu, 'title': "Добавление статьи"})


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


#Берем запись из модели Вимен у которого первичный ключь pk
#если не найдена стр. то ошибка 404 (ф-я get_object_or_404)
#
# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
#     # Параметры которые будут передаватся
#     context = {
#         'post' : post,
#         'menu' : menu,
#         'title' : post.title,
#         'cat_selected' : post.cat_id,
#     }
#     return render(request, 'women/post.html', context=context)


#Создаем клас представлений
class ShowPost(DataMixin,  DetailView):
    model = Women
    template_name = "women/post.html"
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))



class WomenCategory(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return context

# def show_category(request, cat_id):
#     #выбираем с таблицы Women только те у которых   категория общая
#     posts = Women.objects.filter(cat_id=cat_id)
#
#     if len(posts) == 0:
#         raise Http404()
#     context = {
#         'posts': posts,
#         'title': 'Отоброжение по рубрикам',
#         'cat_selected': cat_id,
#     }
#
#     return render(request, 'women/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
