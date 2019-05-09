from django.urls import path
from .views import *
import theme.views

urlpatterns = [
    path('',MainpageView.as_view(), name='mainpage'),
    # path('board',BoardView.as_view(), name="board"),
    path('board',theme.views.boardview, name="board"),
    path('write',theme.views.write, name="write"),
    path('<int:pk>/edit/',theme.views.edit, name="edit"),
    path('<int:pk>/remove/', theme.views.remove, name="remove"),
]