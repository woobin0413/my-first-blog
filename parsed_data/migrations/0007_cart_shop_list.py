# Generated by Django 2.1.5 on 2019-03-02 17:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('parsed_data', '0006_auto_20190302_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='shop_list',
            field=models.ManyToManyField(blank=True, related_name='shop_list', to=settings.AUTH_USER_MODEL),
        ),
    ]
