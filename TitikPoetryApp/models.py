from django.db import models

class Recruit(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	GENDER_CHOICES = (
		('Male', 'Male'),
		('Female', 'Female'),
		)
	gender = models.CharField(max_length=50, choices=GENDER_CHOICES, null=True)
	birthday = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.name

class Tula(models.Model):
	RecId = models.ForeignKey(Recruit, default=None, on_delete=models.CASCADE)
	title_tula = models.CharField(max_length=50)
	text = models.TextField(default="")
	video_file = models.FileField(upload_to='post_files',blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.text
class TitikEnterprise(models.Model):
	RecId = models.ForeignKey(Recruit, default=None, on_delete=models.CASCADE)
	tshirtcode = models.CharField(max_length=50)
	TSHIRT_CHOICES = (
		('Small', 'Small'),
		('Medium', 'Medium'),
		('Large', 'Large'),
		)
	size = models.CharField(max_length=50, choices=TSHIRT_CHOICES, null=True)
	price = models.IntegerField(null=True)
	contact_number = models.IntegerField(null=True)

class ProjectSigya(models.Model):
	RecId = models.ForeignKey(Recruit, default=None, on_delete=models.CASCADE)
	messagebox = models.TextField(default="")
	book_donation = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
	integer = models.IntegerField(null=True)
	date1 = models.DateTimeField(auto_now_add=True)
	
class Comments(models.Model):
	RecId = models.ForeignKey(Recruit, default=None, on_delete=models.CASCADE)
	publications = models.ManyToManyField(Tula)
	comment = models.CharField(max_length=50)
	date2 = models.DateTimeField(auto_now_add=True)