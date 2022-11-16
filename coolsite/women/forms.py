#файл для того чтобы описываь форму реестрации
from django import forms
from .models import *
''' 
клас AddPostForm формы которы будет представлять нашу форму
который наследуется от класа Form
(title,slug, content, is_published, cat) атребути которые будут отображатся на форме
lible заголовки
'''
class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label="Заголовок", widget=forms.TextInput(attrs={'class':'form-input'}))
    slug = forms.SlugField(max_length=255, label="URL")
    content = forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows': 10}), label="Контент")
    is_published = forms.BooleanField(label="Публикация", required=False, initial=True) #required указывает что он не важен
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категории", empty_label="Категория не выбрана")