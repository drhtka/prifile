# Generated by Django 2.2.19 on 2021-03-12 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('create_profile', '0047_auto_20210312_1946'),
    ]

    operations = [
        migrations.RenameField(
            model_name='createbusiness',
            old_name='name',
            new_name='name_bus',
        ),
    ]
