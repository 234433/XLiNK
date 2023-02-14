from django.urls import path
from XLiNK import views
app="XLiNK"
urlpatterns = [
    path('index/', views.index, name="index"),
    path('index/register/', views.register_request, name="register"),
    path('index/login/', views.login_request, name="login"),
    path('index/create/', views.createaccount, name="create"),
    path("community/", views.community, name="community"),
    path("community/create/", views.post, name="post"),
    path('', views.accounts, name="accounts"),
    path('class/create.html/', views.classcreate, name='class' ),
    path('profile.html/id=<int:pk>/', views.home, name="home"),
    path("community/id=<int:pk>/", views.communities, name="communities"),
    path('class/manager/id=<int:pk>/', views.group, name="group"),
    path('community/id=<int:pk>/comment_post.html/',  views.post, name="post"),
    path('', views.IndexView.as_view(), name="accounts"),
    path('class/<slug:name>/', views.posts_by_category, name="class"),
]
