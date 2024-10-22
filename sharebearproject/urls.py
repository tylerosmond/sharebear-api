from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from sharebearapi.views import (
    CategoryViewSet,
    SizeViewSet,
    AgeViewSet,
    WeightViewSet,
    ConditionViewSet,
    ProductViewSet,
    TransactionViewSet,
    WishlistViewSet,
)

router = routers.DefaultRouter(trailing_slash=False)

router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"sizes", SizeViewSet, basename="size")
router.register(r"ages", AgeViewSet, basename="age")
router.register(r"weights", WeightViewSet, basename="weight")
router.register(r"conditions", ConditionViewSet, basename="condition")
router.register(r"products", ProductViewSet, basename="product")
router.register(r"transactions", TransactionViewSet, basename="transaction")
router.register(r"wishlist", WishlistViewSet, basename="wishlist")

urlpatterns = [path("", include(router.urls)), path("admin/", admin.site.urls)]
