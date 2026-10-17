from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .models import Course
from .serializers import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by("id")
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["price"]
    search_fields = ["title"]