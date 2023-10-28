from django.urls import path

from . import views
from .views import RoomList, RoomDetail

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('<slug:slug>/', views.room, name='room'),
    path('rooms_list/', RoomList.as_view(), name='room-list'),
    path('rooms_list/<int:pk>/', RoomDetail.as_view(), name='room-detail'),
]
