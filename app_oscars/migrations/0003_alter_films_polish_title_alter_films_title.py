# Generated by Django 4.0.2 on 2022-02-18 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_oscars', '0002_films_polish_title_alter_films_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='polish_title',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='films',
            name='title',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
    ]