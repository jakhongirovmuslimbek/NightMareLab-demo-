from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("sign-up", views.UserViewSet, basename="sign-up")

urlpatterns = [
    path('users/', include(router.urls)),
]
