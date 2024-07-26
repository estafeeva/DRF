from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from materials.models import Course, Lesson
from users.models import Payments
from users.serializers import (
    PaymentsSerializer,
)


class PaymentsViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filterset_fields = ["course", "lesson", "payment_method"]
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ["payment_date"]
