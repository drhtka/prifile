# Generated by Django 2.2 on 2021-04-04 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city_distr', '0006_auto_20210324_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='rubric',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]
