from django.urls import path
from . import views
urlpatterns = [
    path('exams/',views.exam_view),
    path('fees/',views.fees_view),
    path('attendance/',views.attendance_view),
]