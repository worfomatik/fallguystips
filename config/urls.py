from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from fallguys import views

router = routers.DefaultRouter()
router.register(r'todos', views.todo, 'todo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fallguys/', include(router.urls)),
    path('api/auth/', include('accounts.urls')),
]