from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import GroupMember, Group
from accounts.models import User


# Create your views here.

class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = "chat/home.html"

"""
@login_required
def home(request):
    # group_list = Group.objects
    if request.user.is_authenticated:
        return render(request, "chat/home.html")
    else:
        return redirect("login")
"""


class ChatView(LoginRequiredMixin, generic.TemplateView):
    template_name = "chat/index.html"

"""
@login_required
def index(request):
    if request.user.is_authenticated:
        return render(request, "chat/index.html")
    else:
        return redirect("login")
"""


"""　エラーでわかんない　やりたい事：ログインしたユーザーの所属しているグループを中間テーブル経由で取得して、それをcontextとしてテンプレートに投げたい。
class GroupSelectView(LoginRequiredMixin, generic.TemplateView):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(user_id=request.user.user_id)
        belong = GroupMember.objects.filter(user_id=user.user_id)
        group = Group.objects.filter(group_id=belong)

        return render(request, "chat/group_select.html", {"group": group})
"""


class RoomView(LoginRequiredMixin, generic.TemplateView):
    template_name = "chat/chatroom.html"

"""
@login_required
def chatroom(request, room_name):
    if request.user.is_authenticated:
        return render(request, "chat/chatroom.html", {"room_name": room_name})
    else:
        return redirect("login")
"""