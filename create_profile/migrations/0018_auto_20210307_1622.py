# Generated by Django 2.2.19 on 2021-03-07 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_profile', '0017_auto_20210307_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createneighbour',
            name='gender',
            field=models.CharField(choices=[('1', 'Мужчина'), ('2', 'Женщина'), ('3', '')], default=None, max_length=15, verbose_name='Выбрать пол'),
        ),
    ]
