from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('myapp.urls')),
    path('', lambda request: render(request, 'myapp/index.html'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)