from django.db import models

class Type(models.Model):
	name =models.CharField(max_length=100)
	def __str__(self):
		return self.name

class File(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media/images',blank=True,null=True)
    file =models.FileField(upload_to='media/movies',blank=True,null=True)
    types=models.ForeignKey(Type,
                                on_delete=models.CASCADE)
    description=models.TextField(max_length=1000)
    download_link =models.CharField(max_length=100,blank=True,null=True)
    is_trending=models.BooleanField(default=False)
    is_thriller=models.BooleanField(default=False)
    is_action=models.BooleanField(default=False)
    is_kdrama=models.BooleanField(default=False)
    is_anime=models.BooleanField(default=False)
    is_animation=models.BooleanField(default=False)
    is_horror=models.BooleanField(default=False)



    def __str__(self):
        return self.title


# series/models.py

class Series(models.Model):
    title = models.CharField(max_length=100)
    image=models.ImageField(upload_to='media/images',blank=True,null=True)
    description = models.TextField()
    is_trending=models.BooleanField(default=False)
    is_thriller=models.BooleanField(default=False)
    is_action=models.BooleanField(default=False)
    is_kdrama=models.BooleanField(default=False)
    is_anime=models.BooleanField(default=False)
    is_animation=models.BooleanField(default=False)
    is_horror=models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Episode(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    episode_file = models.FileField(upload_to='episodes/')

    def __str__(self):
        return self.title