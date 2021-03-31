from django.urls import path

from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.ArticlesListView.as_view(), name='index'),
    path('publish/', views.CreateArticleView.as_view(), name='publish'),
]
