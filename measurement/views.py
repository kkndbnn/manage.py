
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView


from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorDetailSerializer, SensorSerializer


class ListCreateView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensUpdateView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class MeasurementCreateView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

