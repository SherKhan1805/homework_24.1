# Generated by Django 5.0.1 on 2024-02-25 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_subscribe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscribe',
            name='course',
        ),
        migrations.RemoveField(
            model_name='subscribe',
            name='user',
        ),
        migrations.DeleteModel(
            name='Payments',
        ),
        migrations.DeleteModel(
            name='Subscribe',
        ),
    ]
