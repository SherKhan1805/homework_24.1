# Generated by Django 4.2.10 on 2024-02-29 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_course_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='дата обновления курса'),
        ),
    ]
