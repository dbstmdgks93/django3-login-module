# Generated by Django 3.1.4 on 2021-01-03 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0010_auto_20210102_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_admin',
        ),
    ]
