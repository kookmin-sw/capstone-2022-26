# Generated by Django 4.0.3 on 2022-05-17 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugs',
            name='b_weight',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='genie',
            name='g_weight',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='melon',
            name='m_weight',
            field=models.FloatField(default=0),
        ),
    ]
