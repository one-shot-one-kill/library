# Generated by Django 4.0.5 on 2022-06-07 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('-created',)},
        ),
    ]