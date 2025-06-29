from django.shortcuts import render
from rest_framework import viewsets
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.
class ListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows listings to be viewed or edited.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

    @swagger_auto_schema(
        operation_description="Retrieve a list of all listings",
        responses={200: ListingSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new listing",
        request_body=ListingSerializer,
        responses={201: ListingSerializer, 400: "Bad Request"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class BookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows bookings to be viewed or edited.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    @swagger_auto_schema(
        operation_description="Retrieve a list of all bookings",
        responses={200: BookingSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new booking",
        request_body=BookingSerializer,
        responses={201: BookingSerializer, 400: "Bad Request"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
