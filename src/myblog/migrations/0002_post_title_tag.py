# Generated by Django 3.1.4 on 2020-12-13 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='TheUpstartcoder', max_length=25),
        ),
    ]
