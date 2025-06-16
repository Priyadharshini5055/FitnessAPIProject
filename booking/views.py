from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import localtime
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingSerializer, BookingCreateSerializer

@api_view(['GET'])
def get_classes(request):
    classes = FitnessClass.objects.filter(start_time__gte=localtime())
    return Response(FitnessClassSerializer(classes, many=True).data)

@api_view(['POST'])
def book_class(request):
    serializer = BookingCreateSerializer(data=request.data)
    if serializer.is_valid():
        try:
            class_obj = FitnessClass.objects.get(id=serializer.validated_data['class_id'])
        except FitnessClass.DoesNotExist:
            return Response({'error': 'Class not found'}, status=status.HTTP_404_NOT_FOUND)

        if class_obj.available_slots <= 0:
            return Response({'error': 'No available slots'}, status=status.HTTP_400_BAD_REQUEST)

        Booking.objects.create(
            fitness_class=class_obj,
            client_name=serializer.validated_data['client_name'],
            client_email=serializer.validated_data['client_email']
        )
        class_obj.available_slots -= 1
        class_obj.save()
        return Response({'success': 'Booking confirmed'}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_bookings(request):
    email = request.GET.get('email')
    if not email:
        return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
    bookings = Booking.objects.filter(client_email=email)
    return Response(BookingSerializer(bookings, many=True).data)