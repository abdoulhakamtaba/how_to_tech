# Generated by Django 3.0.2 on 2020-06-29 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me_blog', '0029_auto_20200629_0313'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
