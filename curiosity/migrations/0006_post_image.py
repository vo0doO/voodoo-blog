# Generated by Django 2.2.4 on 2019-09-24 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curiosity', '0005_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
