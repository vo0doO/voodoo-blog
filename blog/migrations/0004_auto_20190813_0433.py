# Generated by Django 2.2.4 on 2019-08-13 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190813_0431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.Tag'),
        ),
    ]
