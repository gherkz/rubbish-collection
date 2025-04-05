"""
View implementing the Address API endpoints.
"""
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from rubbish_collection.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'street', 'city', 'postcode', 'council']
        read_only_fields = ['id']


class AddressListView(APIView):
    @extend_schema(
        summary="Address lookup",
        description=(
            "Looks up addresses by their component parts, responding with a list of addresses"
        ),
        parameters=[
            OpenApiParameter(name='street', location=OpenApiParameter.QUERY, type=str,
                             description='The street part of the address'),
            OpenApiParameter(name='city', location=OpenApiParameter.QUERY, type=str,
                             description='The city part of the address'),
            OpenApiParameter(name='postcode', location=OpenApiParameter.QUERY, type=str,
                             description='The postcode part of the address'),
        ],
        tags=("Address",),
        responses={
            200: AddressSerializer(many=True)
        },
    )
    def get(self, request, version):
        street = request.query_params.get('street')
        city = request.query_params.get('city')
        postcode = request.query_params.get('postcode')

        addresses = Address.objects.filter(
            street=street,
            city=city,
            postcode=postcode,
        )

        serializer = AddressSerializer(addresses, many=True)

        return Response(serializer.data)

    @extend_schema(
        summary="Create an address",
        description=(
            "Creates an address"
        ),
        tags=("Address",),
        responses={
            200: AddressSerializer
        },
    )
    def post(self, request, version):
        serializer = AddressSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data,
                                status=status.HTTP_201_CREATED)
            return response

        # TODO - return better error messages
        return Response(serializer.errors)
