# Generated by Django 3.2 on 2023-01-10 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['username']},
        ),
    ]
