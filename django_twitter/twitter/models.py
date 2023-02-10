from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	date_posted = models.DateField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
