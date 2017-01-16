from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^/chat/(?P<id>[0-9]+)', ChatView.as_view(), name='chat'),
    url(r'^/chat', ChatsView.as_view(), name='chats'),
]
