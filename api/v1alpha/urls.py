"""
URL routing schema for API

"""
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView
from rest_framework import routers

from api.v1alpha import address_view, rubbish_type_view

app_name = "v1alpha"

router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    # OpenAPI 3 documentation with Swagger UI
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path('addresses/', address_view.AddressListView.as_view(), name='addresses'),
    path('rubbish-types/', rubbish_type_view.RubbishTypeListView.as_view(), name='rubbish_types'),
]
