from django.urls import path

from . import views

urlpatterns = [
    path('', views.package_list, name='index'),
    path('create-package/', views.create_package, name='index'),
    path('package/<int:pk>', views.package, name='index'),
    path('update-package/<int:pk>', views.update_package, name='index'),
    path('delete-package/<int:pk>', views.delete_package, name='index'),
    path('day-details/', views.day_details, name='index'),
    # path('day-details/<str:package_name>', views.package_day_details, name='index'),
    path('create-day-details/', views.create_day_details, name='index'),
    path('update-day-details/<int:pk>', views.update_day_details, name='index'),
    path('delete-day-details/<int:pk>',views.delete_day_details),

    # booking urls
    path('booking/', views.booking, name='index'),
    path('booking/<int:pk>', views.single_booking, name='index'),
    path('update-booking/<int:pk>', views.update_booking, name='index'),
    path('delete-booking/<int:pk>', views.delete_booking, name='index'),



]