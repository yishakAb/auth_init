from django.urls import path
from user import views

app_name = 'user'


urlpatterns = [
    path('create/', views.CreateUser.as_view(), name='create')
]
