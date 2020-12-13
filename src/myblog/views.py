from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy

# Create your views here.
#def home(request):
#    return render (request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-pub_date']
    #ordering = ['-id']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'articles.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = ['title', 'body'] ---> gotten from the models
    #fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html' 
    #fields = ['title', 'title_tag', 'body' ]

class DeletePostView(DeleteView):
    model = Post 
    form_class = PostForm
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')



 