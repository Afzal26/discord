
from django.urls import path
from backend.manage_user import views

urlpatterns = [
    path('create_access', views.create_access),
    path('edit_roles', views.edit_roles)
]
