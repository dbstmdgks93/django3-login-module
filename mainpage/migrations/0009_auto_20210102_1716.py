# Generated by Django 3.1.4 on 2021-01-02 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0008_auto_20210102_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]