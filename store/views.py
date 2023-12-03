from .forms import FeedbackForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpRequest
from datetime import datetime
from django.contrib.auth.forms import AuthenticationForm
from django.db import models
from .models import Blog
from .models import Comment
from .forms import CommentForm
from .forms import BlogForm


def store(request):
    context = {}
    return render(request, 'store/store.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def catalog(request):
    context = {}
    return render(request, 'store/catalog.html', context)


def news(request):
    context = {}
    return render(request, 'store/news.html', context)


def contacts(request):
    context = {}
    return render(request, 'store/contacts.html', context)


def links(request):
    context = {}
    return render(request, 'store/links.html', context)


def videopost(request):
    context = {}
    return render(request, 'store/videopost.html', context)


def forms(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return render(request, 'store/forms.html', {'data': data})
    else:
        form = FeedbackForm()
    return render(request, 'store/forms.html', {'form': form})


def registration(request):
    if request.method == 'POST':
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_staff = False
            reg_f.is_active = True
            reg_f.is_superuser = False
            reg_f.date_joined = datetime.now()
            reg_f.last_login = datetime.now()
            regform.save()
            return redirect('login')
    else:
        regform = UserCreationForm()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'store/registration.html', {'regform': regform, 'year': datetime.now().year, }
    )


def blog(request):
    posts = Blog.objects.all()

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'store/blog.html',
        {
            'title': 'Блог',
            'posts': posts,
            'year': datetime.now().year,
        }
    )


def blogpost(request, parametr):
    assert isinstance(request, HttpRequest)
    post_1 = Blog.objects.get(id=parametr)
    comments = Comment.objects.filter(post=parametr)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user
            comment_f.date = datetime.now()
            comment_f.post = Blog.objects.get(id=parametr)
            comment_f.save()

            return redirect("blogpost", parametr=post_1.id)

    return render(
        request,
        'store/blogpost.html',
        {
            'post_1': post_1,
            'comments': comments,
            'form': form,
            'year': datetime.now().year,
        }
    )


def newpost(request):
    assert isinstance(request, HttpRequest)
    if request.method == "POST":
        blogform = BlogForm(request.POST, request.FILES)
        if blogform.is_valid():
            blog_f = blogform.save(commit=False)
            blog_f.posted = datetime.now()
            blog_f.author = request.user
            blog_f.save()
            return redirect("blog")
    else:
        blogform = BlogForm()
    return render(
        request,
        'store/newpost.html',
        {
            'blogform': blogform,
            'title': "Добавить статью блога",
            'year': datetime.now().year,
        }
    )
