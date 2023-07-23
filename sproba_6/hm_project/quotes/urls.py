from django.urls import path

from . import views

app_name = "quotes"

urlpatterns = [
    path('', views.main, name='root'),
    path('<int:page>', views.main, name='root_paginate'),
    path('authors/<int:author_id>/', views.author_detail, name='author_detail'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('tag/<str:tag_name>/', views.selected_tag, name='selected_tag'),
]