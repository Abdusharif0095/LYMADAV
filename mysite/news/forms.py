from django import forms
from .models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['user_id', 'category_id', 'title', 'content', 'photo']
        widgets = {
            'user_id': forms.Select(attrs={'class': 'form-control'}),
            'category_id': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }


class CommentForm(forms.Form):
    writer = forms.CharField(max_length=150, label='Имя', widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(label='Комментарий', widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))


class SearchForm(forms.Form):
    search_title = forms.CharField(label='', max_length=150, widget=forms.TextInput(attrs={
        'class': "form-control me-2",
        'type': "search",
        'placeholder': "Поиск...",
        'aria-label': "Search",
        'style': 'margin-top: 18px;'
    }))


class RegisterForm(forms.Form):
    fullname = forms.CharField(label='ФИО', max_length="50", widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": "Введите ФИО"}))
    birthday = forms.DateField(label="Дата рождения", widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date',}))
    email = forms.EmailField(label='Электронная Почта', widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": "Введите почту"}))
    password = forms.CharField(max_length=50, label='Пароль', widget=forms.TextInput(attrs={'class': 'form-control', "type": "password", "id": "password", "placeholder": "Введите пароль"}))
    photo = forms.ImageField(label='Фото')
    about = forms.CharField(label='Расскажите о себе', widget=forms.Textarea(attrs={'class': 'form-control', "placeholder": "Напишите немного о себе", 'rows': 5}))
    agree = forms.CharField(label='', widget=forms.CheckboxInput(attrs={
        "type": "checkbox",
        "id": "agreement",
        "style": "transform: scale(1.5); margin-left: 30p;"
    }))
