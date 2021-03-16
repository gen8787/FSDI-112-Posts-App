from django.urls import path
from .views import *

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("post/<int:post_id>/like", like_post, name="like_post"),
    path("post/<int:post_id>/dislike", dislike_post, name="dislike_post")
]
