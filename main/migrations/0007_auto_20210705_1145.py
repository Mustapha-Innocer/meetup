# Generated by Django 3.2.4 on 2021-07-05 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210705_1113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='meetup',
            name='participant',
            field=models.ManyToManyField(blank=True, null=True, to='main.Participant'),
        ),
    ]