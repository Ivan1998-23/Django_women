#файл для того чтобы описываь форму реестрации
from django import forms
from django.core.exceptions import ValidationError

from .models import *
''' 
клас AddPostForm формы которы будет представлять нашу форму
который наследуется от класа Form
(title,slug, content, is_published, cat) атребути которые будут отображатся на форме
lible заголовки
'''
'''
Создаем клас который будет обращатся в СКЛ
 class Meta связывается с класом Women
 fields позволяет отоброжать елементы  на странице 
'''
class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"
    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols':60, 'rows': 10}),
        }

    #Создаем свою проверку елементов на коректность
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return title