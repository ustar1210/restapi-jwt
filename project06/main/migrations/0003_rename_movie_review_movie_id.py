# Generated by Django 4.0.3 on 2022-08-05 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='movie',
            new_name='movie_id',
        ),
    ]
