# Generated by Django 4.0.1 on 2022-05-03 17:07

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_resume_experience_from_year_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='resume_education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(blank=True, default='Null', max_length=2000)),
                ('institute', models.CharField(blank=True, default='Null', max_length=2000)),
                ('details', models.TextField(blank=True, default='Null')),
                ('from_year', models.IntegerField(default='0')),
                ('to_year', models.IntegerField(default='0')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
