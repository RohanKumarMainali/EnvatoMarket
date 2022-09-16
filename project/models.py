from django.db import models
from django.utils.translation import gettext_lazy as _

def upload_to(instance,fileName):
    return 'posts/{fileName}'.format(fileName=fileName)

class Package(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=150)
    days=models.IntegerField(null=True)
    description=models.CharField(max_length=500)
    price=models.IntegerField( null=True)
    seat=models.IntegerField( null=True)
    category=models.CharField(max_length=50,null=True)
    image=models.ImageField(_("image"),upload_to=upload_to )

    def __str__(self):
        return self.name
# Create your models here.