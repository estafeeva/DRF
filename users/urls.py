from django.urls import path
from rest_framework.routers import SimpleRouter
from django.contrib import admin
from django.urls import path, include
from users.apps import UsersConfig
from users.views import (
    PaymentsViewSet,
)

app_name = UsersConfig.name

router = SimpleRouter()
router.register("payments", PaymentsViewSet)

urlpatterns = []

urlpatterns += router.urls
