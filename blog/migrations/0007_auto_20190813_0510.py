# Generated by Django 2.2.4 on 2019-08-13 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190813_0438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]