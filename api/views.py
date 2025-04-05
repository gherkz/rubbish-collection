"""
A view which exposes the available versions of the API.

"""

from django.urls.base import reverse
from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from .versions import AVAILABLE_VERSIONS, VERSIONS_TO_APP_NAME


def build_version_response_schema():
    """
    Returns a response schema that can be used with `inline_serializer` to construct
    a response schema for the auto generated OpenAPI docs.

    """

    return {version_name: serializers.CharField() for version_name in AVAILABLE_VERSIONS}


class VersionsView(APIView):
    # Disable versioning for this viewset as there will not be a 'version' param
    # in the url.
    versioning_class = None

    @extend_schema(
        summary="List API Versions",
        description=(
            "Lists the available versions of the API, responding with a dictionary of version "
            "name to the url that version can be accessed at"
        ),
        tags=("API Versions",),
        responses={
            200: inline_serializer(name="APIVersions", fields=build_version_response_schema())
        },
    )
    def get(self, request):
        return Response(
            {
                version: request.build_absolute_uri(
                    reverse(f"{app_name}:api-root", args=[version])
                )
                for version, app_name in VERSIONS_TO_APP_NAME.items()
            }
        )
