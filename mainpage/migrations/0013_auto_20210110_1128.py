# Generated by Django 3.1.4 on 2021-01-10 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0012_auto_20210109_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('남성', '남성'), ('여성', '여성')], default='', max_length=20, null=True),
        ),
    ]