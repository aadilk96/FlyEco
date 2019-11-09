from django.urls import path
from . import views
from . import query

urlpatterns = [
    path('', views.home, name='flyeco-home'),
    path('about/', views.about, name='flyeco-about'),
    # path('search/', views.search, name='flyeco-search')
]
