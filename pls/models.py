from django.db import models
import datetime
from django.core.exceptions import ValidationError

def file_size(value): # add this to some file where you can import it from
    limit = 100* 1024 
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 100 KB.')


def user_path(instance,filename):
	return 'Picture Of_{0}/{1}'.format(instance, filename)

def party_path(instance,filename):
	return 'Party Symbol of _{0}/{1}'.format(instance,filename)    

def can_path(instance,filename):
	return 'Photo of _{0}/{1}'.format(instance,filename)    

def picture_path(instance,filename):
	return 'Picture of _{0}/{1}'.format(instance,filename)    

class facility(models.Model):
	class Meta:
		verbose_name_plural='Facilities'
	fname=models.CharField(max_length=100)
	def __str__(self):
		return self.fname
		
class pollingStation(models.Model):
	name=models.CharField(max_length=100,default='')
	pid=models.CharField(max_length=100)
	password=models.CharField(max_length=100,default='')
	lat=models.FloatField(default=0)
	lon=models.FloatField(default=0)
	address=models.CharField(max_length=500,default='')
	no=models.IntegerField(default=0)
	fName=models.ManyToManyField(facility)
	picture=models.ImageField(upload_to=user_path,null=True,blank=True,validators=[file_size])
	def __str__(self):
		return self.pid		
		
class Candidate(models.Model):
	name=models.CharField(max_length=100)
	photo=models.ImageField(upload_to=can_path,null=True,blank=True,validators=[file_size])
	party=models.CharField(max_length=100,default='')
	symbol=models.ImageField(upload_to=party_path,null=True,blank=True,validators=[file_size])
	affitavid=models.CharField(max_length=1000,default='')
	vote=models.IntegerField(default=0)
	def __str__(self):
		return self.party

class pickupPoint(models.Model):
	name=models.CharField(max_length=100,default='')
	pickupLat=models.FloatField(default=0)
	pickupLon=models.FloatField(default=0)
	pickupTime=models.TimeField(default=datetime.time(16,00))
	picture=models.ImageField(upload_to=picture_path,null=True,blank=True,validators=[file_size])
	address=models.CharField(max_length=500,default='')
	
	def __str__(self):
		return self.name


class pwd(models.Model):
	class Meta:
		verbose_name_plural="(special voters) Divyangs"
	epic=models.CharField(max_length=10)
	phone=models.BigIntegerField(default=0)
	point=models.OneToOneField(pickupPoint,on_delete=models.CASCADE,null=True)
	
	def __str__(self):
		return self.epic

class ThirdGender(models.Model):
	class Meta:
		verbose_name_plural="(special voters) Third Genders"
	epic=models.CharField(max_length=10)
	phone=models.BigIntegerField(default=0)
	point=models.OneToOneField(pickupPoint,on_delete=models.CASCADE,null=True)
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

