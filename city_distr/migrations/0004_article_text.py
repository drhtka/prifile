# Generated by Django 2.2 on 2021-03-24 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city_distr', '0003_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='text',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
