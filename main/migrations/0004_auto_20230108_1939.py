# Generated by Django 3.2 on 2023-01-08 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_file_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/images'),
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='media/movies'),
        ),
    ]
