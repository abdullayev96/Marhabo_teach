from django.urls import path
from .views import *

app_name = 'articles'
urlpatterns = [
    path('',HomePageView.as_view(), name = 'home'),
    path('new/',ArticleCreateView.as_view(), name='article_new' ),
    path('<int:pk>/',ArticleDetailView.as_view(),name = 'article_detail'),
    path('list/',ArticleListView.as_view(), name = 'article_list'),
    path('<int:pk>/delete/',  ArticleDeleteView.as_view(), name = 'article_delete'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name= 'article_edit'),
    path('<str:category_name>/category',ArticleCategoryView.as_view(),name = 'category'),
    # path('<str:pk>/category',ArticleCategoryView.as_view(),name = 'category'),
    path('<int:pk>/category/',ArticleCategoryDetail.as_view(), name='article_category'),
]
