# Generated by Django 5.0.7 on 2024-07-25 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, help_text='Tell us something about yourself.', max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, help_text='Where are you from?', max_length=60),
        ),
    ]
