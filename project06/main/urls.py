from django.urls import path
from .views import *
from . import views

app_name="main"
urlpatterns = [
    path('', views.movie_list_create),
    path('<int:movie_pk>/', views.movie_detail_update_delete),
    path('<int:movie_pk>/review/',views.review_list_create),
    path('review/<int:review_pk>/', views.review_detail_delete),
]