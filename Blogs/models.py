from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=250)
    images = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.title

    def description_small(self):
        return self.description[:300]

    def post_time(self):
        return self.pub_date.strftime('%A %B %-d %Y')
