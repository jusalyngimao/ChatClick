from django.urls import path
from .views import ReceiveMessageAPIView

urlpatterns = [
    path('receive/', ReceiveMessageAPIView.as_view(), name='receive_message'),
]
