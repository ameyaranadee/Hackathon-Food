# Generated by Django 3.0.8 on 2020-10-17 09:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('NGO', '0019_auto_20201017_0051'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('Other_Specifics', models.TextField(default='Punjabi,Chinese,Mexican', max_length=100)),
                ('images', models.ImageField(blank=True, null=True, upload_to='NGO/images')),
                ('city', models.CharField(default='enter', max_length=100)),
                ('pickup_address', models.TextField(max_length=20)),
                ('created_on', models.DateTimeField(null=True)),
                ('edible', models.IntegerField(default=0)),
                ('measurement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='NGO.Measurement')),
                ('otherDetails', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='NGO.otherDetails')),
                ('typee', models.ForeignKey(default='veg', null=True, on_delete=django.db.models.deletion.CASCADE, to='NGO.TypeOf')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='foodsss', related_query_name='foodsss', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]