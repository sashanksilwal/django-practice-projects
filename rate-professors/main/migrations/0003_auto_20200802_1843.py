# Generated by Django 3.0.8 on 2020-08-02 18:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200802_1841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorial',
            name='published_date',
        ),
        migrations.AddField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_slug',
            field=models.CharField(default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='tutorialcategory',
            name='category_slug',
            field=models.CharField(default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='tutorialseries',
            name='series_summary',
            field=models.CharField(max_length=200),
        ),
    ]