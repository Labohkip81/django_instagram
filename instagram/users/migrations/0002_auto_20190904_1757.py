# Generated by Django 2.1 on 2019-09-04 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instagramuser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
