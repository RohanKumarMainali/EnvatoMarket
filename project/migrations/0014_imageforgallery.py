# Generated by Django 4.1.1 on 2022-09-18 07:17

from django.db import migrations, models
import django.db.models.deletion
import project.models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0013_alter_daydetails_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageForGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=project.models.upload_to, verbose_name='image')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.package')),
            ],
        ),
    ]
