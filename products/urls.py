from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("categories", views.CategoryViewSet,          basename="categories")
router.register("subcategories", views.SubCategoryViewSet,    basename="subcategories")
router.register("tags", views.TagViewSet,                     basename="tags")
router.register("bodycategories", views.BodyCategoryViewSet,  basename="bodycategories")
router.register("animations", views.AnimationViewSet,         basename="animations")

urlpatterns = [
    path('products/', include(router.urls)),
]
