# Generated by Django 3.2 on 2023-02-11 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_episode_series'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='is_action',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='file',
            name='is_animation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='file',
            name='is_anime',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='file',
            name='is_horror',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='file',
            name='is_kdrama',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='file',
            name='is_thriller',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='file',
            name='is_trending',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='series',
            name='is_action',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='series',
            name='is_animation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='series',
            name='is_anime',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='series',
            name='is_horror',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='series',
            name='is_kdrama',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='series',
            name='is_thriller',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='series',
            name='is_trending',
            field=models.BooleanField(default=False),
        ),
    ]
