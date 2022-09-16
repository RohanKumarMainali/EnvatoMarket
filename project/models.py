from django.db import models
from django.utils.translation import gettext_lazy as _

def upload_to(instance,fileName):
    return 'posts/{fileName}'.format(fileName=fileName)

class Package(models.Model):
    name=models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, unique=True,null=True)
    days=models.IntegerField(null=True)
    description=models.TextField(max_length=2500)
    departure_return_location = models.CharField(max_length=200,null=True)
    departure_time = models.CharField(max_length=300,null=True)
    return_time= models.CharField(max_length=300,null=True)
    price=models.IntegerField( null=True)
    package_included = models.CharField(max_length=100,null=True)
    package_excluded = models.CharField(max_length=200,null=True)
    seat=models.IntegerField( null=True)
    category=models.CharField(max_length=50,null=True)
    image=models.ImageField(_("image"),upload_to=upload_to )



    def __str__(self):
        return self.name
# Create your models here.

class Booking(models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=750)
    phone_number=models.IntegerField( null=True)
    check_out= models.DateField(null=True)
    number_of_people=models.IntegerField(null=True)
    enquiry = models.TextField(null=True)


    def __str__(self):
        return self.name

CHOICES =(
    (1, "One"),
    (2, "Two"),
    (3, "Three"),
    (4, "Four"),
    (5, "Five"),
    (6, "Six"),
    (7, "Seven"),
    (8, "Eight"),
    (9, "Nine"),
    (10, "Ten"),
    (11, "Eleven"),
    (12, "Tweleve"),
    (13, "Thirteen"),
    (14, "Fourteen"),
    (15, "Fifteen"),
    (16, "SixTeen"),
    (17, "SevenTeen"),
    (18, "Eighteen"),
    (19, "Ninteen"),
    (20, "Twenty"),

)
class DayDetails(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    day = models.IntegerField(choices=CHOICES, default=1)
    title = models.CharField(max_length=500,null=True)
    description = models.TextField(max_length=5000,null=True)