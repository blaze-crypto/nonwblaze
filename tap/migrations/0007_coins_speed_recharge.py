# Generated by Django 5.0.7 on 2024-07-15 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tap', '0006_tasks_task_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='coins',
            name='speed_recharge',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
