from django.urls import path
from .views.auth import AuthView

urlpatterns = [
    path('auth/', AuthView.as_view(), name='auth'),
]
