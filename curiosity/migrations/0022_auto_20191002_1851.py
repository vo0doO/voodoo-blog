# Generated by Django 2.2.4 on 2019-10-02 15:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('curiosity', '0021_auto_20191002_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.UUIDField(default=uuid.UUID('aef49513-86db-447b-b5e0-a724acd98417'), primary_key=True, serialize=False, verbose_name='Интификатор'),
        ),
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение'),
        ),
    ]
