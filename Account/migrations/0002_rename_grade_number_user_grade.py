# Generated by Django 4.0.5 on 2022-08-26 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='grade_number',
            new_name='grade',
        ),
    ]
