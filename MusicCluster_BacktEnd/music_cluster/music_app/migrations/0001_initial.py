# Generated by Django 5.0.7 on 2024-07-23 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('favorite_genre', models.CharField(max_length=100)),
                ('listening_hours_per_week', models.IntegerField()),
                ('favorite_artist', models.CharField(max_length=100)),
                ('concert_attendance', models.BooleanField()),
                ('device_preference', models.CharField(choices=[('P', 'Phone'), ('C', 'Computer'), ('T', 'Tablet')], max_length=1)),
            ],
        ),
    ]
