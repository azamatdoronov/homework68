from django.urls import path

from .views import ArticleView

app_name = 'api_v2'

urlpatterns = [
    path('article/', ArticleView.as_view(), name='ArticleView'),
    path('article/<int:pk>/', ArticleView.as_view(), name='ArticleView'),
]
