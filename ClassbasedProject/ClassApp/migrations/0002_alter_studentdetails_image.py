# Generated by Django 4.2.4 on 2024-06-02 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClassApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='image',
            field=models.FileField(upload_to='images/'),
        ),
    ]
