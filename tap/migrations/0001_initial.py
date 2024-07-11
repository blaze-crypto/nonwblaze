# Generated by Django 5.0.7 on 2024-07-11 11:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Boosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boost_title', models.CharField(blank=True, max_length=255, null=True)),
                ('boost_price', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Boost',
                'verbose_name_plural': 'Boosts',
                'db_table': 'boosts',
            },
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(blank=True, max_length=255, null=True)),
                ('task_description', models.TextField(blank=True, null=True)),
                ('task_price', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
                'db_table': 'tasks',
            },
        ),
        migrations.CreateModel(
            name='Coins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coins', models.IntegerField(blank=True, default=0, null=True)),
                ('coin_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Coins',
                'verbose_name_plural': 'Coins',
                'db_table': 'coins',
            },
        ),
        migrations.CreateModel(
            name='UserBoost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=1)),
                ('boost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tap.boosts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Boost',
                'verbose_name_plural': 'User Boosts',
                'db_table': 'user_boosts',
            },
        ),
    ]
