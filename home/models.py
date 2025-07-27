from django.db import models


class Job(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Home(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    job = models.ForeignKey(
        Job, on_delete=models.PROTECT, related_name='home_job', null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name
