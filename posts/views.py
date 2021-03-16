from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "all_posts_list"


# ---- L I K E   P O S T
def like_post(request, post_id):
    liked_post = Post.objects.get(id=post_id)
    liked_post.likes += 1
    liked_post.save()
    return redirect('/')


# ---- D I S L I K E   P O S T
def dislike_post(request, post_id):
    disliked_post = Post.objects.get(id=post_id)
    disliked_post.dislikes += 1
    disliked_post.save()
    return redirect('/')
