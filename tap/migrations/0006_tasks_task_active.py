# Generated by Django 5.0.7 on 2024-07-13 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tap', '0005_tasks_task_url_alter_boosts_boost_icon_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='task_active',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
