# Generated by Django 4.1.1 on 2022-09-16 06:21

from django.db import migrations, models
import project.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('days', models.IntegerField(null=True)),
                ('description', models.CharField(max_length=500)),
                ('price', models.IntegerField(null=True)),
                ('seat', models.IntegerField(null=True)),
                ('category', models.CharField(max_length=50, null=True)),
                ('image', models.ImageField(upload_to=project.models.upload_to, verbose_name='image')),
            ],
        ),
    ]
