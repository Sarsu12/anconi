# Generated by Django 3.1.7 on 2021-04-19 23:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20210419_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portafolio',
            name='image',
            field=models.ImageField(default='portafolio/default.png', upload_to='portafolio', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png'])], verbose_name='Imagen'),
        ),
    ]