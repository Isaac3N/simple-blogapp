# Generated by Django 3.1.4 on 2020-12-14 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0006_auto_20201214_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Clink link above to read bog post', max_length=355),
        ),
    ]
