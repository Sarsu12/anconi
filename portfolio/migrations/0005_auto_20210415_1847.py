# Generated by Django 3.1.7 on 2021-04-15 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_portafolio_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portafolio',
            name='image',
            field=models.ImageField(default='portafolio/default.png', upload_to='portafolio'),
        ),
    ]
