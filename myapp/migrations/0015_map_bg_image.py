# Generated by Django 4.0.1 on 2022-04-28 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_map_remove_contact_map'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='bg_image',
            field=models.CharField(blank=True, default='Null', max_length=2000),
        ),
    ]
