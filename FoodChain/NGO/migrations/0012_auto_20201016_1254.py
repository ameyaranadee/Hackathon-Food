# Generated by Django 3.0.8 on 2020-10-16 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NGO', '0011_otherdetails_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otherdetails',
            name='image',
            field=models.ImageField(upload_to='NGO/images'),
        ),
    ]