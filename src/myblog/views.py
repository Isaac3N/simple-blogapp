from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

# Create your views here.
#def home(request):
#    return render (request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'articles.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    #fields = ['title', 'body'] ---> gotten from the models
    fields = '__all__'