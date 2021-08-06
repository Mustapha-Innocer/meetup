# Generated by Django 3.2.4 on 2021-07-04 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_meetpup_meetup'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='description',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meetup',
            name='slug',
            field=models.SlugField(default=None, unique=True),
            preserve_default=False,
        ),
    ]