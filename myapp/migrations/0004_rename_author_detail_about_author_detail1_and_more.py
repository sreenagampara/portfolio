# Generated by Django 4.0.1 on 2022-04-22 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_about'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='author_detail',
            new_name='author_detail1',
        ),
        migrations.AddField(
            model_name='about',
            name='author_detail10',
            field=models.CharField(default='Null', max_length=1000),
        ),
        migrations.AddField(
            model_name='about',
            name='author_detail2',
            field=models.CharField(default='Null', max_length=1000),
        ),
        migrations.AddField(
            model_name='about',
            name='author_detail3',
            field=models.CharField(default='Null', max_length=1000),
        ),
        migrations.AddField(
            model_name='about',
            name='author_detail4',
            field=models.CharField(default='Null', max_length=1000),
        ),
        migrations.AddField(
            model_name='about',
            name='author_detail5',
            field=models.CharField(default='Null', max_length=1000),
        ),
        migrations.AddField(
            model_name='about',
            name='author_detail6',
            field=models.CharField(default='Null', max_length=1000),
        ),
        migrations.AddField(
            model_name='about',
            name='author_detail7',
            field=models.CharField(default='Null', max_length=1000),
        ),
        migrations.AddField(
            model_name='about',
            name='author_detail8',
            field=models.CharField(default='Null', max_length=1000),
        ),
        migrations.AddField(
            model_name='about',
            name='author_detail9',
            field=models.CharField(default='Null', max_length=1000),
        ),
    ]
