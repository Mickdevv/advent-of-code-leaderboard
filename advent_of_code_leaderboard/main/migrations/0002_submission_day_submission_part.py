# Generated by Django 4.2.13 on 2024-11-28 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='day',
            field=models.IntegerField(choices=[(1, 'Day 1'), (2, 'Day 2'), (3, 'Day 3'), (4, 'Day 4'), (5, 'Day 5'), (6, 'Day 6'), (7, 'Day 7'), (8, 'Day 8'), (9, 'Day 9'), (10, 'Day 10'), (11, 'Day 11'), (12, 'Day 12'), (13, 'Day 13'), (14, 'Day 14'), (15, 'Day 15'), (16, 'Day 16'), (17, 'Day 17'), (18, 'Day 18'), (19, 'Day 19'), (20, 'Day 20'), (21, 'Day 21'), (22, 'Day 22'), (23, 'Day 23'), (24, 'Day 24'), (25, 'Day 25')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='submission',
            name='part',
            field=models.IntegerField(choices=[(1, 'Part 1'), (2, 'Part 2')], default=2),
            preserve_default=False,
        ),
    ]
