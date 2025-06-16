from django.urls import path
from . import views

urlpatterns = [
    path('public/', views.public_view),
    path('test/', views.test_view),
]
