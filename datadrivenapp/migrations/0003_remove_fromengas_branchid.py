# Generated by Django 3.1.2 on 2020-10-29 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datadrivenapp', '0002_auto_20201029_1931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fromengas',
            name='BRANCHID',
        ),
    ]
