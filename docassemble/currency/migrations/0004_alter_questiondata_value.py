# Generated by Django 4.1 on 2022-08-23 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0003_alter_questiondata_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questiondata',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
    ]
