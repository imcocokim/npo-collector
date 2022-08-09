# Generated by Django 4.1 on 2022-08-09 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_npo_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='npo',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='npo',
            name='website',
            field=models.URLField(max_length=250),
        ),
    ]