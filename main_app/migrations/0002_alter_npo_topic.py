# Generated by Django 4.1 on 2022-08-09 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='npo',
            name='topic',
            field=models.CharField(choices=[('AN', 'Animal Protection & Welfare'), ('EV', 'Environment'), ('ED', 'Education'), ('H', 'Health'), ('HC', 'Human & Civil Rights'), ('HS', 'Human Services'), ('I', 'International Relief')], default='AN', max_length=2),
        ),
    ]
