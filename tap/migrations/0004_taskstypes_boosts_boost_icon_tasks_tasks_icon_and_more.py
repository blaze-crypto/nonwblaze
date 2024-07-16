# Generated by Django 5.0.7 on 2024-07-12 13:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tap', '0003_coins_energy_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='TasksTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_title', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Task Type',
                'verbose_name_plural': 'Task Types',
                'db_table': 'tasks_types',
            },
        ),
        migrations.AddField(
            model_name='boosts',
            name='boost_icon',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='/boost_icons'),
        ),
        migrations.AddField(
            model_name='tasks',
            name='tasks_icon',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='/tasks_icon'),
        ),
        migrations.AddField(
            model_name='tasks',
            name='tasks_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tap.taskstypes'),
        ),
    ]