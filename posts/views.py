from django.views.generic import ListView, DetailView
from .models import Post 

class PostListView(ListView):
    template_name ="post_list.html"
    model = Post 

class PostDetailView(DetailView):
    template_name = "post_detail.html"
    model = Post 