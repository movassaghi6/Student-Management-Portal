# Generated by Django 3.2.12 on 2022-04-16 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_auto_20220416_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newapp',
            name='code_pish_niaz',
            field=models.FloatField(blank=True, null=True, verbose_name='کد پيش نيازها'),
        ),
    ]