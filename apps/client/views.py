from django.shortcuts import render

from rest_framework import viewsets

from .serializers import ClientSerializers
from .models import Client

from django.core.exceptions import PermissionDenied


class ClientViewset(viewsets.ModelViewSet):
    serializer_class = ClientSerializers
    queryset = Client.objects.all()

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        obj = self.get_object()

        if self.request.user != obj.created_by:
            raise PermissionDenied('Wrong object owner')

        serializer.save()