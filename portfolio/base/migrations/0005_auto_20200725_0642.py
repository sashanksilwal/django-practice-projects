# Generated by Django 3.0.8 on 2020-07-25 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20200725_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]