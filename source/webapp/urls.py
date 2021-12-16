from django.urls import path

from webapp.views import index_view, create_articles_views

urlpatterns = [
    path('', index_view),
    path('articles/add/', create_articles_views)
]
