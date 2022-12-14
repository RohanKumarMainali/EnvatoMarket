# Generated by Django 4.1.1 on 2022-09-16 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_package_departure_return_location_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=750)),
                ('phone_number', models.IntegerField(null=True)),
                ('check_out', models.DateField(null=True)),
                ('number_of_people', models.IntegerField(null=True)),
                ('enquiry', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DayDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five')], default=1)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.package')),
            ],
        ),
    ]
