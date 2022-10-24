from django.urls import path

from measurement.views import ListSensorView, ModifyView, CreateMeasureView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', ListSensorView.as_view()),
    path('sensors/<pk>/', ModifyView.as_view()),
    path('measurements/', CreateMeasureView.as_view())
]
