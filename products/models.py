from django.db import models
from PIL import Image
# Create your models here.

class Teams(models.Model):
	name=models.CharField(max_length=20);
	Matches=models.CharField(max_length=10);
	ranking=models.TextField();
	players=models.TextField();


class Rankig(models.Model):
	odiposition=models.CharField(max_length=20);
	name = models.ForeignKey(Teams, models.DO_NOTHING , db_column='name' , blank=True , null=True) 
	odirating = models.CharField(max_length=20);


class Testrankig(models.Model):
	
	name = models.ForeignKey(Teams, models.DO_NOTHING , db_column='name' , blank=True , null=True) 
	rating = models.CharField(max_length=20);


class Ground(models.Model):
	name= models.CharField(max_length=20);
	opened = models.CharField(max_length=20);
	capacity = models.CharField(max_length=20);
	ends = models.CharField(max_length=20);
	location = models.CharField(max_length=20);
	floodlights = models.CharField(max_length=20);
	image=models.ImageField(upload_to="gallery");

class Stats(models.Model):
	name=models.CharField(max_length=10,blank=True);
	ame= models.CharField(max_length=10,blank=True); 
	played=models.CharField(max_length=10);
	namewins=models.CharField(max_length=10);
	amewins=models.CharField(max_length=10);
	tie=models.CharField(max_length=10);
	abcscore=models.CharField(max_length=30,blank=True);
	bcdscoree=models.CharField(max_length=30,blank=True);
	abcbat=models.CharField(max_length=30,blank=True);
	bcdbatt=models.CharField(max_length=30,blank=True);
	abcbowl=models.CharField(max_length=30,blank=True);
	bcdbowll=models.CharField(max_length=30,blank=True);
	image=models.ImageField(upload_to="gallery",blank=True);
	imagee=models.ImageField(upload_to="gallery",blank=True);


class Runs(models.Model):
	name=models.CharField(max_length=50);
	ame=models.CharField(max_length=50);
	matches=models.CharField(max_length=50);
	Scores= models.CharField(max_length=50);
	country=models.CharField(max_length=50);
	image=models.ImageField(upload_to="gallery",blank=True);



class Playerstat(models.Model):
	name=models.CharField(max_length=50);
	ame=models.CharField(max_length=50);
	# born=models.CharField(max_length=50);
	# birthplace=models.CharField(max_length=50);
	# teams = models.CharField(max_length=50);
	# profile=models.CharField(max_length=500);
	matches=models.CharField(max_length=50);
	Scores=models.CharField(max_length=50);
	country=models.CharField(max_length=50);
	image=models.ImageField(upload_to="gallery",blank=True);