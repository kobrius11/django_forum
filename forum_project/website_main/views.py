from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import PostForm

# Create your views here.
class PostsListView(ListView):
    model = Post
    template_name = 'index.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["posts"] = self.model.objects.all()
        return context

class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        #TODO
        return super().get(request, *args, **kwargs)
    

class PostCreateView(CreateView, LoginRequiredMixin):
    form_class = PostForm

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        #TODO
        return super().get(request, *args, **kwargs)
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        #TODO
        return super().post(request, *args, **kwargs)
    

