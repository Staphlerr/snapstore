# Generated by Django 5.1 on 2024-09-17 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_moodentry_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moodentry',
            old_name='time',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='moodentry',
            old_name='feelings',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='moodentry',
            old_name='mood',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='moodentry',
            old_name='mood_intensity',
            new_name='price',
        ),
    ]
