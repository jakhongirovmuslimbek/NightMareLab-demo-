from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("user-type", views.UserTypeViewSet,           basename="user-type")
router.register("categories", views.CategoryViewSet,          basename="categories")
router.register("subcategories", views.SubCategoryViewSet,    basename="subcategories")
router.register("tags", views.TagViewSet,                     basename="tags")
router.register("bodycategories", views.BodyCategoryViewSet,  basename="bodycategories")
router.register("animations", views.AnimationViewSet,         basename="animations")
router.register("request_type", views.RequestTypeViewSet,     basename="request_type")
router.register("request", views.RequestViewSet,              basename="request")
router.register("company", views.CompanyViewSet,              basename="company")

urlpatterns = [
    path('v1/', include(router.urls)),
]
