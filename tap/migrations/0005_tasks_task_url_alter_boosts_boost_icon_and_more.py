# Generated by Django 5.0.7 on 2024-07-12 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tap', '0004_taskstypes_boosts_boost_icon_tasks_tasks_icon_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='task_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='boosts',
            name='boost_icon',
            field=models.ImageField(blank=True, null=True, upload_to='boost_icons/'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='tasks_icon',
            field=models.ImageField(blank=True, null=True, upload_to='tasks_icon/'),
        ),
    ]
