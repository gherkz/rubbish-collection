"""
View implementing the Collection Schedule API endpoints.
"""
from datetime import date

from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import serializers, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from rubbish_collection import models
from rubbish_collection.models import CollectionSchedule, Address, RubbishType


class RubbishTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RubbishType
        fields = ['name']
        read_only_fields = ['id']


class CollectionScheduleSerializer(serializers.ModelSerializer):
    rubbish_type = RubbishTypeSerializer()

    class Meta:
        model = models.CollectionSchedule
        fields = ['id', 'rubbish_type', 'frequency', 'start_date', 'import_date']
        read_only_fields = ['id', 'import_date']

    def create(self, validated_data):
        print(type(validated_data))
        address_id = self.context.get('address_id')
        address = get_object_or_404(Address, pk=address_id)

        rubbish_type = get_object_or_404(RubbishType, name=validated_data['rubbish_type']['name'])
        validated_data.pop('rubbish_type')

        return CollectionSchedule.objects.create(address=address,
                                                 rubbish_type=rubbish_type,
                                                 import_date=date.today(),
                                                 **validated_data)


class CollectionScheduleListView(APIView):
    @extend_schema(
        summary="Collection schedule retrieval",
        description=(
            "Retrieves a list of collection schedules for the given address"
        ),
        parameters=[
            OpenApiParameter(name='address_id', location=OpenApiParameter.PATH, type=str,
                             description='The ID of the address to fetch collection schedules for'),
        ],
        tags=("Collection Schedule",),
        responses={
            200: CollectionScheduleSerializer(many=True)
        },
    )
    def get(self, request, version, address_id):
        collection_schedules = CollectionSchedule.objects.filter(address_id=address_id)

        serializer = CollectionScheduleSerializer(collection_schedules, many=True)

        return Response(serializer.data)

    @extend_schema(
        summary="Create a collection schedule",
        description=(
            "Creates a collection schedule for this address"
        ),
        tags=("Collection Schedule",),
        responses={
            200: CollectionScheduleSerializer
        },
    )
    def post(self, request, version, address_id):
        serializer = CollectionScheduleSerializer(data=request.data, context={
            'address_id': address_id,
        })

        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data,
                                status=status.HTTP_201_CREATED)
            return response

        # TODO - return better error messages
        return Response(serializer.errors)
