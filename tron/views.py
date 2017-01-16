from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, get_object_or_404

from .models import ChatRoom


class ChatView(View):

    @staticmethod
    def get(request, **args):
        chat = get_object_or_404(ChatRoom, pk=args['id'])
        return render(request, 'tron/chat.html', {'chat': chat})


class ChatsView(View):

    @staticmethod
    def get(request):
        chat_rooms = ChatRoom.objects.order_by('name')
        context = {
            'chat_list': chat_rooms
        }
        return render(request, 'tron/chats.html', context)
