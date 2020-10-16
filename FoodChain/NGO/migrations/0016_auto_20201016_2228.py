# Generated by Django 3.0.8 on 2020-10-16 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NGO', '0015_auto_20201016_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='veg', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='foodavbl',
            name='FoodKind',
            field=models.TextField(default='veg', max_length=100),
        ),
        migrations.AddField(
            model_name='foodavbl',
            name='image',
            field=models.ImageField(default='/media/imp.png', upload_to='NGO/images'),
        ),
        migrations.AddField(
            model_name='foodavbl',
            name='typee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='NGO.options'),
        ),
    ]