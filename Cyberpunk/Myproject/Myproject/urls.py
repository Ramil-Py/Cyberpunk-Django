from django.contrib import admin
from django.urls import path, include
from myapp.views import page_not_found, about, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('about/', about),
    path('', index)
]

handler404 = page_not_found