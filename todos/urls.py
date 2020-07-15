from django.urls import path

from .views import HomePageView, TodoCreateView, TodoDeleteView

urlpatterns = [
    path('item/<int:pk>/delete/', TodoDeleteView.as_view(), name='todo_delete'),
    path('todo/new/', TodoCreateView.as_view(), name='todo_new'),
    path('', HomePageView.as_view(), name='home'),
]