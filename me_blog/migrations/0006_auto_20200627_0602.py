# Generated by Django 3.0.2 on 2020-06-27 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me_blog', '0005_auto_20200627_0600'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='featured',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='overview',
            field=models.TextField(blank=True, null=True),
        ),
    ]
