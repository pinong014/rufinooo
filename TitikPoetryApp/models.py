from django.db import models

class Recruit(models.Model):
	name = models.CharField(max_length=50, null=True)
	email = models.EmailField(max_length=50, null=True)
	GENDER_CHOICES = (
		('Male', 'Male'),
		('Female', 'Female'),
		)
	gender = models.CharField(max_length=50, choices=GENDER_CHOICES, null=True)
	birthday = models.DateTimeField()
	def __str__(self):
		return self.name

class Tula(models.Model):
	RecId = models.ForeignKey(Recruit, null=True, on_delete= models.SET_NULL)
	title_tula = models.CharField(max_length=50)
	text = models.TextField(default="")
	video_file = models.FileField(upload_to='post_files',blank=True, null=True)
	def __str__(self):
		return self.text

class ProjectSigya(models.Model):
	RecId = models.ForeignKey(Recruit, null=True, on_delete= models.SET_NULL)
	messagebox = models.TextField(default="")
	book_donation = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
	integer = models.IntegerField(null=True)
	date1 = models.DateTimeField()
	
class Comments(models.Model):
	RecId = models.ForeignKey(Recruit, null=True, on_delete= models.SET_NULL)
	publications = models.ManyToManyField(Tula)
	comment = models.CharField(max_length=50)
	date2 = models.DateTimeField(auto_now_add=True)






	