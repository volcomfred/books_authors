
# from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('books_authors_app.urls')),
]
