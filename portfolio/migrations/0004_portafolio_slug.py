# Generated by Django 3.1.7 on 2021-04-14 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20210414_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='portafolio',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]