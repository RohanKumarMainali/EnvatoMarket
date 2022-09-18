from django.contrib import admin
from .models import *

class AdminDaysInline(admin.StackedInline):
    # list_display = ('package', 'day', 'title','description')
    model = DayDetails
    extra = 0


class AdminBooking(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number','check_out','number_of_people','enquiry')
admin.site.register(Booking, AdminBooking)

# Register your models here.
class AdminPackage(admin.ModelAdmin):
    list_display=('name','days','price','seat','category')
    inlines = [AdminDaysInline]
admin.site.register(Package,AdminPackage)

class AdminTestimonial(admin.ModelAdmin):
    list_display = ['author_name','description','image']
# admin.site.register(DayDetails)
admin.site.register(Testimonial,AdminTestimonial)
admin.site.register(GradeChoice)

