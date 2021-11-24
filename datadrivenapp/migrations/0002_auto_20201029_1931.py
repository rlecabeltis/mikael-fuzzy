# Generated by Django 3.1.2 on 2020-10-29 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datadrivenapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fromengas',
            name='ADA_NO',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='fromengas',
            name='CHECK_NO',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterModelTable(
            name='agency',
            table='r_agency',
        ),
        migrations.AlterModelTable(
            name='fromengas',
            table='t_engas',
        ),
        migrations.AlterModelTable(
            name='fromlbp',
            table='t_lbp',
        ),
    ]
