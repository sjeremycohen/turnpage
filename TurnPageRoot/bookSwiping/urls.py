from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path('bookshelf/', views.BookshelfView.as_view(), name="mybookshelf"),
    path('liked/', views.liked_book, name="liked_book"),
]
