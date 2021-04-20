# Generated by Django 3.1.7 on 2021-04-20 00:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_categoria_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portafolio',
            name='image',
            field=models.ImageField(upload_to='portafolio', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png'])], verbose_name='Imagen'),
        ),
    ]