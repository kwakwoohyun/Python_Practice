# Generated by Django 2.2.1 on 2019-06-07 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0003_auto_20190603_0748'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
