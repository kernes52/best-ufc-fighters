from django.db.models import Q
from django.db.models.deletion import ProtectedError
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Fighter, WeightClass, Event, Bout
from .serializers import FighterSerializer, WeightClassSerializer, EventSerializer, BoutSerializer

class FightersListCreate(APIView):
    def get(self, request):
        qs = Fighter.objects.all().order_by('id')
        ser = FighterSerializer(qs, many=True)
        return Response(ser.data)
    def post(self, request):
        ser = FighterSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

class FighterDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Fighter, pk=pk)
    def get(self, request, pk):
        obj = self.get_object(pk)
        ser = FighterSerializer(obj)
        return Response(ser.data)
    def patch(self, request, pk):
        obj = self.get_object(pk)
        ser = FighterSerializer(obj, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        obj = self.get_object(pk)
        try:
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError:
            return Response({'detail': 'Cannot delete fighter with bouts or favorites'}, status=status.HTTP_400_BAD_REQUEST)

class WeightClassesListCreate(APIView):
    def get(self, request):
        qs = WeightClass.objects.all().order_by('id')
        ser = WeightClassSerializer(qs, many=True)
        return Response(ser.data)
    def post(self, request):
        ser = WeightClassSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

class WeightClassDetailByCode(APIView):
    def get_object(self, code):
        return get_object_or_404(WeightClass, code=code)
    def get(self, request, code):
        obj = self.get_object(code)
        ser = WeightClassSerializer(obj)
        return Response(ser.data)
    def patch(self, request, code):
        obj = self.get_object(code)
        ser = WeightClassSerializer(obj, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, code):
        obj = self.get_object(code)
        try:
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError:
            return Response({'detail': 'Cannot delete weight class with fighters'}, status=status.HTTP_400_BAD_REQUEST)

class EventsListCreate(APIView):
    def get(self, request):
        qs = Event.objects.all().order_by('date')
        ser = EventSerializer(qs, many=True)
        return Response(ser.data)
    def post(self, request):
        ser = EventSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

class EventDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Event, pk=pk)
    def get(self, request, pk):
        obj = self.get_object(pk)
        ser = EventSerializer(obj)
        return Response(ser.data)
    def patch(self, request, pk):
        obj = self.get_object(pk)
        ser = EventSerializer(obj, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        obj = self.get_object(pk)
        try:
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError:
            return Response({'detail': 'Cannot delete event with bouts'}, status=status.HTTP_400_BAD_REQUEST)

class BoutsListCreate(APIView):
    def get(self, request):
        fighter_id = request.query_params.get('fighter_id')
        qs = Bout.objects.all()
        if fighter_id:
            qs = qs.filter(Q(fighter_red_id=fighter_id) | Q(fighter_blue_id=fighter_id))
        ser = BoutSerializer(qs, many=True)
        return Response(ser.data)
    def post(self, request):
        ser = BoutSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

class BoutDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Bout, pk=pk)
    def get(self, request, pk):
        obj = self.get_object(pk)
        ser = BoutSerializer(obj)
        return Response(ser.data)
    def patch(self, request, pk):
        obj = self.get_object(pk)
        ser = BoutSerializer(obj, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
