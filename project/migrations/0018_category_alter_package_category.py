# Generated by Django 4.1.1 on 2022-09-18 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0017_blog_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='package',
            name='category',
            field=models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.category'),
        ),
    ]
