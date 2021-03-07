from django.db import models

# Create your models here.

class homework(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	pdf = models.FileField(upload_to='hw/pdfs/')

	def __str__(self):
		return self.title







