# Generated by Django 3.2.12 on 2022-04-17 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0011_alter_daneshjo_tarikh_tavalod'),
    ]

    operations = [
        migrations.CreateModel(
            name='info_dars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dars_info', models.CharField(blank=True, max_length=255, null=True, verbose_name='اطلاعات درس')),
                ('info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='newapp.newapp', verbose_name='درس')),
            ],
        ),
    ]
