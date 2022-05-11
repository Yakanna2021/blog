from django.urls  import reverse_lazy
from django.shortcuts import render
from .models import *
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = "blocks_app/home.html"

class DetailView(DetailView):
    model = Post
    template_name = "blocks_app/post_details.html"


class CreateView(CreateView):
    model = Post
    template_name = "blocks_app/post_new.html"
    fields='__all__'
    
    def form_isvalid(self,form):
        if  form.is_valid():
            form.save()
        return redirect('')    
class UpdateView(UpdateView):
    model = Post
    template_name = "blocks_app/post_edit.html"
    fields=["title","summary"]
    
class DeleteView(DeleteView):
    model = Post
    template_name = "blocks_app/delete_post.html"
    success_url=reverse_lazy('home')

