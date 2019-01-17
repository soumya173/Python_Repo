from django.db import models

class Task(models.Model):
	task_name = models.CharField(max_length=100)
	task_desc = models.CharField(max_length=100)
	date_created = models.DateTimeField(auto_now=True)
	is_completed = models.BooleanField(default=False)


