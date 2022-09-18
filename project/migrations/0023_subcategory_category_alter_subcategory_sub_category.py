# Generated by Django 4.1.1 on 2022-09-18 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0022_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.category'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='sub_category',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
