# Generated by Django 4.0 on 2022-07-19 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myproduct',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
