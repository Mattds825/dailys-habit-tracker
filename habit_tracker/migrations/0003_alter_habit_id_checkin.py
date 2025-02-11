# Generated by Django 5.1.4 on 2025-02-11 09:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit_tracker', '0002_habit_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='CheckIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked_in_on', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField()),
                ('habit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='check_ins', to='habit_tracker.habit')),
            ],
        ),
    ]
