# Generated by Django 2.2.4 on 2019-08-03 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='user',
            new_name='user_id',
        ),
    ]
