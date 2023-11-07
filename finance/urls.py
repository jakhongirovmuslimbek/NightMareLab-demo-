from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("payment", views.PaymentViewSet, basename="payment")

urlpatterns = [
    path('finance/', include(router.urls)),
]
