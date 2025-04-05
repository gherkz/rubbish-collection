"""
View implementing the Rubbish Type API endpoints.
"""
from drf_spectacular.utils import extend_schema
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from rubbish_collection.models import RubbishType


class RubbishTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RubbishType
        fields = ['id', 'name']
        read_only_fields = ['id']


class RubbishTypeListView(APIView):
    @extend_schema(
        summary="Lists rubbish types",
        description=(
            "Lists all available rubbish types"
        ),
        tags=("Rubbish Type",),
        responses={
            200: RubbishTypeSerializer(many=True)
        },
    )
    def get(self, request, version):
        rubbish_types = RubbishType.objects.all()

        serializer = RubbishTypeSerializer(rubbish_types, many=True)

        return Response(serializer.data)

    @extend_schema(
        summary="Create a new rubbish type",
        description=(
            "Creates a new rubbish type"
        ),
        tags=("Rubbish Type",),
        responses={
            200: RubbishTypeSerializer
        },
    )
    def post(self, request, version):
        serializer = RubbishTypeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data,
                                status=status.HTTP_201_CREATED)
            return response

        # TODO - return better error messages
        return Response(serializer.errors)
