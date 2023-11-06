# forms.py к примеру

from django import forms
from .models import News, Posts

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'text', 'description', 'counter']

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'text', 'likes']


# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Posts
from .forms import NewsForm, PostsForm


def news_new(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = NewsForm()
    return render(request, 'news_edit.html', {'form': form})

def posts_new(request):
    if request.method == "POST":
        form = PostsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostsForm()
    return render(request, 'posts_edit.html', {'form': form})