from django.urls import path
from measurement.views import ListCreateView, SensUpdateView, MeasurementCreateView

urlpatterns = [
    path('listsens/', ListCreateView.as_view()),
    path('sensors/<int:pk>/', SensUpdateView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
    # path('senscreate/', SensorCreateView.as_view(())),
]
