# Generated by Django 3.0.2 on 2020-06-27 06:06

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('me_blog', '0007_blogpost_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='content',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
