# Generated by Django 4.1.1 on 2022-09-25 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0025_remove_package_subcategory_delete_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]