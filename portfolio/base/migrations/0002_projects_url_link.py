# Generated by Django 3.0.8 on 2020-07-23 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='url_link',
            field=models.TextField(blank=True),
        ),
    ]
