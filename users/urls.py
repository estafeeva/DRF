from django.urls import path
from rest_framework.routers import SimpleRouter
from django.contrib import admin
from django.urls import path, include
from users.apps import UsersConfig
from users.views import (
    PaymentsViewSet,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.views import UserCreateAPIView

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

app_name = UsersConfig.name

router = SimpleRouter()
router.register("payments", PaymentsViewSet)

"""urlpatterns = []

urlpatterns += router.urls"""


