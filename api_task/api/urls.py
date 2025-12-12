from django.urls import path
from .views import get_user, create_user, delete_user, update_user

urlpatterns = [
    path('users/', get_user, name='get-user'),
    path('users/create/', create_user, name='create-user'),
    path('users/<int:pk>/delete/', delete_user, name='delete-user'),
    path('users/<int:pk>/update/', update_user, name='update-user'),

]   