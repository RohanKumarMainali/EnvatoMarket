# Generated by Django 4.1.1 on 2022-09-27 08:39

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0029_package_additional_information'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='description',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
