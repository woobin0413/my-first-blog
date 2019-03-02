# Generated by Django 2.1.5 on 2019-03-02 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parsed_data', '0005_auto_20190301_0228'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('quantity', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='like',
            name='post',
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.AddField(
            model_name='cart',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts', to='parsed_data.Post'),
        ),
    ]
