# Generated by Django 4.0.4 on 2022-05-31 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0006_advert_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='hours',
            field=models.CharField(default='date', max_length=100),
        ),
    ]
