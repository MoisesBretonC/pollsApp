# Generated by Django 5.0.5 on 2024-05-20 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Choise',
            new_name='Choice',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='choise_text',
            new_name='choice_text',
        ),
    ]
