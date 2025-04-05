"""
URL routing schema for API

"""
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView
from rest_framework import routers

app_name = "v1alpha"

router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    # OpenAPI 3 documentation with Swagger UI
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
]
