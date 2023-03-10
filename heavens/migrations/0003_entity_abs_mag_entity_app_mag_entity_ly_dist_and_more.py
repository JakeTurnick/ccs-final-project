# Generated by Django 4.1.7 on 2023-03-10 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heavens', '0002_alter_entity_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='abs_mag',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entity',
            name='app_mag',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entity',
            name='ly_dist',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entity',
            name='spec_class',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
