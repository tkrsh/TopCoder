# Generated by Django 3.1.4 on 2021-01-07 23:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratings',
            name='language',
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='links',
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='location',
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='rating',
        ),
        migrations.AddField(
            model_name='ratings',
            name='city',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ratings',
            name='country',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ratings',
            name='organization',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ratings',
            name='our_rating',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ratings',
            name='rank_codechef',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ratings',
            name='rank_codeforces',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ratings',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='rating_codechef',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='rating_codeforces',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]
