# Generated by Django 2.1.5 on 2019-02-27 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsed_data', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='image/%Y/%m/%d'),
        ),
    ]
