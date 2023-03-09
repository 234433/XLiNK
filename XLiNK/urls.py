from django.urls import path
from XLiNK import views
from django.urls import reverse
app="XLiNK"
urlpatterns = [
    path('index/', views.index, name="index"),
    path('index/register/', views.register_request, name="register"),
    path('index/login/', views.login_request, name="login"),
    path('index/create/', views.CreateAccountView.as_view(), name="create"),
    path('community/', views.communitys, name="communitys"),
    path('community/<slug:name>/comment_post/',  views.CommentFromView.as_view(), name="form"),
    path('', views.accounts, name="accounts"),
    path('class/create.html/', views.CreateClassView.as_view(), name='class' ),
    path('profile.html/id=<int:pk>/', views.home, name="home"),
    path('community/<str:name>/', views.community, name="community"),
    path('follow_count', views.follow_count, name="follow_count"),
    path('class/manager/id=<int:pk>/', views.group, name="group"),
    path('', views.IndexView.as_view(), name="accounts"),
    path('class/<slug:name>/', views.posts_by_category, name="class"),
]
