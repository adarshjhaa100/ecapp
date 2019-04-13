from django.db import models
import datetime


def user_path(instance,filename):
	return 'Picture Of_{0}/{1}'.format(instance, filename)

def party_path(instance,filename):
	return 'Party Symbol of _{0}/{1}'.format(instance,filename)    

def can_path(instance,filename):
	return 'Photo of of _{0}/{1}'.format(instance,filename)    

class facility(models.Model):
	class Meta:
		verbose_name_plural='Facilities'
	fname=models.CharField(max_length=100)
	def __str__(self):
		return self.fname
		
class pollingStation(models.Model):
	pid=models.CharField(max_length=100)
	password=models.CharField(max_length=100,default='')
	lat=models.FloatField(default=0)
	lon=models.FloatField(default=0)
	address=models.CharField(max_length=500,default='')
	no=models.IntegerField(default=0)
	fName=models.ManyToManyField(facility)
	picture=models.ImageField(upload_to=user_path,null=True,blank=True)
	def __str__(self):
		return self.pid		
		
class Candidate(models.Model):
	name=models.CharField(max_length=100)
	photo=models.ImageField(upload_to=can_path,null=True,blank=True)
	party=models.CharField(max_length=100,default='')
	symbol=models.ImageField(upload_to=party_path,null=True,blank=True)
	affitavid=models.CharField(max_length=1000,default='')
	def __str__(self):
		return self.party

class pwd(models.Model):
	class Meta:
		verbose_name_plural="(special voters) Divyangs"
	epic=models.CharField(max_length=10)
	phone=models.BigIntegerField(default=0)
	pickupLat=models.FloatField(default=0)
	pickupLon=models.FloatField(default=0)
	pickupTime=models.TimeField(default=datetime.time(16,00))
	def __str__(self):
		return self.epic

class ThirdGender(models.Model):
	class Meta:
		verbose_name_plural="(special voters) Third Genders"
	epic=models.CharField(max_length=10)
	phone=models.BigIntegerField(default=0)
	pickupLat=models.FloatField(default=0)
	pickupLon=models.FloatField(default=0)
	pickupTime=models.TimeField(default=datetime.time(16,00))
	def __str__(self):
		return self.epic

class Suggestion(models.Model):
	text=models.CharField(max_length=1000,default='')
	rating=models.FloatField(default=0)
	def __str__(self):
		return self.text

class result(models.Model):
	candidate=models.CharField(max_length=100,default='')
	votes=models.IntegerField(default=0)
	party=models.CharField(max_length=100,default='')
	def __str__(self):
		return self.candidate

