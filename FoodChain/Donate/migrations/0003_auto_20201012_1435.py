# Generated by Django 3.0.8 on 2020-10-12 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donate', '0002_auto_20201012_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodreq',
            name='foodtakenfrom',
            field=models.IntegerField(default=0, max_length=250),
        ),
        migrations.AlterField(
            model_name='foodreq',
            name='quantity_required',
            field=models.IntegerField(default=0),
        ),
    ]
