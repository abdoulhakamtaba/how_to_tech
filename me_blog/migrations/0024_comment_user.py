# Generated by Django 3.0.2 on 2020-06-28 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('me_blog', '0023_auto_20200628_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='me_blog.Author'),
        ),
    ]
