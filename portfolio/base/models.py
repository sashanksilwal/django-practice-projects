from django.db import models


class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url_link = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title