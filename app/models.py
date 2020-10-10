from django.db import models

# Create your models here.

# Table to store all the data
class DataModel(models.Model):
	task_id=models.IntegerField()
	timestamp=models.DateTimeField()
	temperature=models.FloatField()
	duration=models.CharField(max_length=255)

	def __str__(self):
		return self.task_id

# table to store the visitor track i.e. requested user ip and time
class VisitTracker(models.Model):
	ip=models.CharField(max_length=20)
	request_datetime=models.DateTimeField()
	
	def __str__(self):
		return self.ip