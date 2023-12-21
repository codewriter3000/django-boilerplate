from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.UserList.as_view(), name='home'),
    path('<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('create/', views.UserCreate.as_view(), name='user_create'),
    path('login/', views.UserLogin.as_view(), name='user_login'),
    path('logout/', views.UserLogout.as_view(), name='user_logout'),
]
