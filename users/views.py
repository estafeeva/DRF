from django.shortcuts import render
from django.urls import reverse_lazy
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from materials.models import Course, Lesson
from users.models import Payments, User
from users.serializers import PaymentsSerializer, UserSerializer
from users.services import (
    create_stripe_product,
    create_stripe_price,
    create_stripe_session,
)


class PaymentsViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filterset_fields = ["course", "lesson", "payment_method"]
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ["payment_date"]

    def perform_create(self, serializer):
        success_url = "http://127.0.0.1:8000/" + reverse_lazy("users:payments-list")

        payment = serializer.save()
        payment.owner = self.request.user
        stripe_product = create_stripe_product(payment)
        stripe_price = create_stripe_price(stripe_product, payment.payment_sum)
        stripe_session = create_stripe_session(stripe_price, success_url)

        payment.payment_link = stripe_session.get("url")
        payment.session_id = stripe_session.get("id")

        payment.save()


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
