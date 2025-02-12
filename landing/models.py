from django.db import models

# Create your models here.

class About (models.Model):
    heading = models.CharField(max_length=100)
    subheading = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.heading

class Feature (models.Model):
    for_about = models.ForeignKey(About, on_delete=models.CASCADE, related_name="features")
    feature_title = models.CharField(max_length=100)
    feature_description = models.TextField()
    
    def __str__(self):
        return self.feature_title