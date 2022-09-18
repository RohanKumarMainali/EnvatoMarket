from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

def upload_to(instance,fileName):
    return 'posts/{fileName}'.format(fileName=fileName)

class GradeChoice(models.Model):
    choice = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.choice

class Package(models.Model):
    name=models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, unique=True,null=True)
    days=models.IntegerField(null=True)
    description=RichTextField(blank=True,null=True)
    departure_location = models.CharField(max_length=200,null=True)
    return_location = models.CharField(max_length=200,null=True)
    departure_time = models.CharField(max_length=300,null=True)
    return_time= models.CharField(max_length=300,null=True)
    price=models.IntegerField( null=True)
    package_included = models.TextField(max_length=100,null=True)
    package_excluded = models.TextField(max_length=200,null=True)
    max_altitude = models.IntegerField(null=True)
    seat=models.IntegerField(null=True)
    category=models.CharField(max_length=50,null=True)
    grade = models.ForeignKey(GradeChoice, on_delete=models.CASCADE,null=True)
    image=models.ImageField(_("image"),upload_to=upload_to )

    def __str__(self):
        return self.name

class ImageForGallery(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    image = models.ImageField(_("image"),upload_to=upload_to)


class Booking(models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=750)
    phone_number=models.IntegerField( null=True)
    check_out= models.DateField(null=True)
    number_of_people=models.IntegerField(null=True)
    enquiry = models.TextField(null=True)


    def __str__(self):
        return self.name

class DayChoice(models.Model):
    day = models.CharField(max_length=200)

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
    (21, "Twenty One"),
    (22, "Twenty Two"),
    (23, "Twenty Three"),
    (24, "Twenty Four"),
    (25, "Twenty Five"),
    (26, "Twenty Six"),
    (27, "Twenty Seven"),
    (28, "Twenty Eight"),
    (29, "Twenty Nine"),
    (30, "Thirty"),
)
class DayDetails(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    day = models.IntegerField(choices=CHOICES, default=1)
    title = models.CharField(max_length=500,null=True)
    description = models.TextField(max_length=5000,null=True)

  

class Testimonial(models.Model):
    author_name = models.CharField(max_length=300,default="admin")
    description = models.TextField(max_length=5000,null=True)
    image = models.ImageField(_("image"),upload_to=upload_to)

    def __str__(self):
        return self.author_name 

class Blog(models.Model):
    author_name = models.CharField(max_length=300,null=True)
    title = models.CharField(max_length=500,null=True)
    image = image=models.ImageField(_("image"),upload_to=upload_to,null=True)
    description = RichTextField(blank=True,null=True)
    posted_on = models.DateTimeField(auto_now_add=True, blank=True)

    