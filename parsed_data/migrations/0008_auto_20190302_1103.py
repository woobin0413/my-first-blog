# Generated by Django 2.1.5 on 2019-03-02 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsed_data', '0007_cart_shop_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='post',
        ),
        migrations.AlterField(
            model_name='cart',
            name='shop_list',
            field=models.ManyToManyField(blank=True, related_name='shop_list', to='parsed_data.Post'),
        ),
    ]
