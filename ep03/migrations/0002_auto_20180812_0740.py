# Generated by Django 2.1 on 2018-08-12 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ep03', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-id',)},
        ),
    ]