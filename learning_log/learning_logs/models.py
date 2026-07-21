from django.db import models

# Create your models here.
#Code wise a model is just a class, it has attribute and methods, just like every class we have discussed. 
class Topic (models.Model):
      """A topic the user is learning about"""
      text = models.CharField(max_length=200)
      date_added = models.DateTimeField(auto_now_add=True)  

def __str__(self):
      """Return a string representation of the model."""
      return self.text




