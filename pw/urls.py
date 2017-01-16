from django.conf.urls import url, include
# from django.contrib import admin

urlpatterns = [
    url(r'^tron', include('tron.urls', namespace='tron')),
]
