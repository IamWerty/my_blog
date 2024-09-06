from django.shortcuts import render
from .models import Post
# Create your views here.
def post_list(request):
    post_list = Post.objects.all()
    return render(request, "blogapp/posts_list.html", {"posts_list":post_list})