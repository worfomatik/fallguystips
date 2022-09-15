from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import TodoSerializer
# from .models import Todo

# Create your views here.

class todo(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    # queryset = Todo.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):  # added
        return self.request.user.todos.all()

    def perform_create(self, serializer):  # added
        serializer.save(owner=self.request.user)