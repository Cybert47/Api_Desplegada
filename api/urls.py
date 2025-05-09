from django.contrib import admin
from django.urls import path
from api.views import authors_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/', authors_view),
]
