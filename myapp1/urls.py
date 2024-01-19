from django.urls import path
from myapp1 import views
 

urlpatterns = [
    path('',views.register,name="register"),
    path("user_login/",views.user_login,name="user_login"),
    path("user_logout/",views.user_logout,name='user_logout'),
    path("profil/",views.profile,name='profil'),
    path("jabpost/",views.job_posts,name='jobpost'),
    path("daily/",views.daily_posts,name='daily'),
    path("homepro/",views.homepro,name='homepro'),
    path("blog/",views.blog,name='blog'),
    path("bdetail/<int:pk>/",views.jdetails,name='bdetail'),
    path("search/",views.search,name="search"),
    path("likes/<int:pk>/",views.like_post,name="likes"),
    path("booked/<int:pk>/",views.booked,name="booked"),
    path("liked/",views.likes,name='liked'),
    path("bookmarks/",views.bookmark,name='bookmarks'),
]
