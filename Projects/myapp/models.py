

# Create your models here.
from django.db import models
from time import time
# Create your models here.
#from django.db import models

# Create your models here.
def get_upload_file_name(instance, filename):
    return "uploaded_file/%s_%s" %(str(time()).replace('.','_'), filename)
class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    thumbnail = models.FileField(upload_to=get_upload_file_name)
    def __str__(self):
        return self.name