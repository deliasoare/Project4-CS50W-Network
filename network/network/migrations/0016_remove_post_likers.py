# Generated by Django 4.1.2 on 2023-01-03 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0015_post_likers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likers',
        ),
    ]
