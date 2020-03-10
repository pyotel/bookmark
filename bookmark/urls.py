from django.urls import path
from .views import BookmarkListView
from .views import BookmarkCreateView
from .views import BookmarkDetailView
from .views import BookmarkUpdateView
from .views import BookmarkDeleteView

urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>', BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name='delete'),
]