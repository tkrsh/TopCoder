# Generated by Django 3.1.4 on 2021-01-07 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210107_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratings',
            name='email_user',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
