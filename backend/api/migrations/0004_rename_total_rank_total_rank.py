# Generated by Django 4.0.3 on 2022-05-20 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_total_weight'),
    ]

    operations = [
        migrations.RenameField(
            model_name='total',
            old_name='total_rank',
            new_name='rank',
        ),
    ]
