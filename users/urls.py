from . import views
from django.urls import path

urlpatterns = [
    path('', views.UserList.as_view(), name='home'),
    path('<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
]
