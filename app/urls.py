from django.urls import path
from . import views

app_name: str = 'app'
urlpatterns = [
    path('', views.index_view, name='index-view'),
    path('about/', views.about_view, name='about-view')
]
