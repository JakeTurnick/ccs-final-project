# Generated by Django 4.1.7 on 2023-03-09 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_type', models.CharField(choices=[('star', 'Star'), ('const', 'Constellation'), ('mtshr', 'Meteor Shower'), ('comet', 'Comet'), ('plnt', 'Planet'), ('hcrft', 'Human Craft')], max_length=5)),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateField(blank=True)),
                ('ra', models.CharField(max_length=50)),
                ('dec', models.CharField(max_length=50)),
            ],
        ),
    ]