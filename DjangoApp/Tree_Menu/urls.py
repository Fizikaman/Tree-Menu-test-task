from django.urls import path

from .views import TreeMenuView

urlpatterns = [
    path('', TreeMenuView.as_view()),
    path('<slug:slug>', TreeMenuView.as_view(), name='Tree_Menu'),
]

