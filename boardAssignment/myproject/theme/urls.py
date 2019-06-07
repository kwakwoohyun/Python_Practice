from django.urls import path
from .views import *
import theme.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',MainpageView.as_view(), name='mainpage'),
    # path('board',BoardView.as_view(), name="board"),
    path('board',theme.views.boardview, name="board"),
    path('write',theme.views.write, name="write"),
    path('<int:pk>/edit/',theme.views.edit, name="edit"),
    path('<int:pk>/remove/', theme.views.remove, name="remove"),
    path('<int:blog_id>/detaile/', theme.views.detaile, name="detaile"),
    path('<int:pk>/<int:blog_id>/comment_remove/',theme.views.comment_remove, name="comment_remove"),
    path('<int:blog_id>/<int:comment_id>/comment_edit/',theme.views.comment_edit, name="comment_edit"),
    path('hashtag',theme.views.hashtagform, name="hashtag"),
    path('<int:hashtag_id>/search/', theme.views.search, name="search"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)