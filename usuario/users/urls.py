from django.urls import path,include
from users.views import UserView


urlpatterns = [
    path('users/',UserView.as_view(),name="user"),
    path('users/<int:pk>/', UserView.as_view(), name='user-detail'),
    
]