# Generated by Django 5.0.7 on 2024-07-17 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tap', '0009_friends_inviite_price_alter_friends_friends'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friends',
            old_name='inviite_price',
            new_name='invite_price',
        ),
    ]
