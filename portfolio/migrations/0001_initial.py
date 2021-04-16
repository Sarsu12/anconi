# Generated by Django 3.1.7 on 2021-04-12 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Portafolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=25)),
                ('descripcion', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='portafolio')),
                ('fecha', models.DateField(auto_now=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.categoria')),
            ],
        ),
    ]
