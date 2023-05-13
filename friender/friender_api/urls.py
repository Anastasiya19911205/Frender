from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('establishments/',EstablishmentsListAPIView.as_view()),
    path('establishments/<int:pk>/', EstablishmentsListAPIViewDetail.as_view())
]