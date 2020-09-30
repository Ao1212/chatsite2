from django.urls import path
from . import views

app_name = "chat"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("chat/", views.ChatView.as_view(), name="index"),
    path("chat/<str:room_name>/", views.RoomView.as_view(), name="room"),
    path("groupselect/", views.GroupSelectView.as_view(), name="group_select")
]
