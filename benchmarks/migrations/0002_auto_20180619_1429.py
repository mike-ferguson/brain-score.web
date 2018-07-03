# Generated by Django 2.0.5 on 2018-06-19 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benchmarks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatemodel',
            name='behavior',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidatemodel',
            name='brain_score',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidatemodel',
            name='imagenet_top1',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidatemodel',
            name='it',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidatemodel',
            name='v4',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]