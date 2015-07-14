import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published',default=timezone.now())
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

	def __str__(self):
		return self.question_text

class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):              # __unicode__ on Python 2
		return self.choice_text

class Leciono(models.Model):
	def __str__(self):
		return str(self.id)
	numero	= models.IntegerField(default=0)
	
class Teksto(models.Model):
	leciono	= models.ForeignKey(Leciono)
	teksto	= models.TextField()

class Vorto(models.Model):
	leciono	= models.ForeignKey(Leciono)
	vorto	= models.CharField(max_length=56)
	rimarko	= models.CharField(max_length=56,blank=True)
	traduko	= models.CharField(max_length=56)
	

class Noto(models.Model):
	leciono	= models.ForeignKey(Leciono)
	noto	= models.TextField()
