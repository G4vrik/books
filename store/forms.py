from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.db import models
from .models import Comment
from .models import Blog

class FeedbackForm(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=100)
    email = forms.EmailField(label='Email')
    rate_site = forms.ChoiceField(label='Оцените сайт',
                                  choices=[(5, 'Отлично'), (4, 'Хорошо'), (3, 'Удовлетворительно'), (2, 'Плохо'),
                                           (1, 'Очень плохо')], widget=forms.RadioSelect)
    rate_content = forms.ChoiceField(label='Оцените контент',
                                     choices=[(5, 'Отлично'), (4, 'Хорошо'), (3, 'Удовлетворительно'), (2, 'Плохо'),
                                              (1, 'Очень плохо')], widget=forms.RadioSelect)
    rate_design = forms.ChoiceField(label='Оцените дизайн',
                                    choices=((5, 'Отлично'), (4, 'Хорошо'), (3, 'Удовлетворительно'), (2, 'Плохо'),
                                             (1, 'Очень плохо')))

    feedback = forms.CharField(label='Ваш отзыв', widget=forms.Textarea, required=False)

    # Добавляем чекбоксы
    subscribe = forms.BooleanField(label='Подписаться на новости', required=False)
    notifications = forms.BooleanField(label='Получать уведомления', required=False)

    # Добавляем список
    wishes = forms.MultipleChoiceField(
        label='Что вы хотели бы увидеть на сайте?',
        choices=[
            ('articles', 'Новые статьи'),
            ('videos', 'Видео'),
            ('live', 'Прямые эфиры'),
            ('projects', 'Новые проекты'),
        ],
        widget=forms.CheckboxSelectMultiple, required=False
    )


class BootstrapAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({'class': 'form-control', 'placeholder': 'User name'}))
    password = forms.CharField(label=('Password'),
                               widget=forms.PasswordInput({'class': 'form-control', 'placeholder': 'Password'}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)
        labels = {"text": "Комментарий"}


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ("title", "description", "content", "image",)
        labels = {"title": "Заголовок", "description": "Краткое содержание", "content": "Полное содержание", "image": "Картинка"}
