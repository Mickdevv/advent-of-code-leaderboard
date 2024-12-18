# Generated by Django 4.2.13 on 2024-11-30 21:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='uploads/')),
                ('day', models.IntegerField(choices=[(1, 'Day 1'), (2, 'Day 2'), (3, 'Day 3'), (4, 'Day 4'), (5, 'Day 5'), (6, 'Day 6'), (7, 'Day 7'), (8, 'Day 8'), (9, 'Day 9'), (10, 'Day 10'), (11, 'Day 11'), (12, 'Day 12'), (13, 'Day 13'), (14, 'Day 14'), (15, 'Day 15'), (16, 'Day 16'), (17, 'Day 17'), (18, 'Day 18'), (19, 'Day 19'), (20, 'Day 20'), (21, 'Day 21'), (22, 'Day 22'), (23, 'Day 23'), (24, 'Day 24'), (25, 'Day 25')])),
                ('part', models.IntegerField(choices=[(1, 'Part 1'), (2, 'Part 2')])),
                ('code', models.FileField(upload_to='uploads/text_files/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
