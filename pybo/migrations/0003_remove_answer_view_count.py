# Generated by Django 4.0.3 on 2023-05-23 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0002_question_view_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='view_count',
        ),
    ]
