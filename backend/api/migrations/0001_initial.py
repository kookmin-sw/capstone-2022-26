# Generated by Django 4.0.3 on 2022-05-01 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('sid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('rank', models.CharField(max_length=50)),
                ('song', models.CharField(max_length=50)),
                ('artist', models.CharField(max_length=50)),
                ('like', models.CharField(max_length=50)),
                ('coverImg', models.URLField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('artist', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=30)),
                ('img_url', models.URLField(unique=True)),
                ('daybefore_rank', models.IntegerField()),
                ('yesterday_rank', models.IntegerField()),
                ('today_rank', models.IntegerField()),
            ],
        ),
    ]
