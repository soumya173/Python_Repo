from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# import django_filters.rest_framework.filters
from .serializers import TaskSerializers
from .models import Task

class TaskViewSet(viewsets.ModelViewSet):
	queryset = Task.objects.all().order_by("-date_created")
	serializer_class = TaskSerializers

	filter_backend = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
	filter_fields = ("is_completed",)
	ordering = ("-date_created",)

	search_fields = ("task_name",)

"""
class DueTaskViewSet(viewsets.ModelViewSet):
	# queryset = Task.objects.get(is_completed=False)
	queryset = Task.objects.all().order_by("-date_created").filter(is_completed=False)
	serializer_class = TaskSerializers

class CompletedTaskViewSet(viewsets.ModelViewSet):
	queryset = Task.objects.all().order_by("-date_created").filter(is_completed=True)
	serializer_class = TaskSerializers
"""

