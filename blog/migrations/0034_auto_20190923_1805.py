# Generated by Django 2.2.4 on 2019-09-23 15:05

from django.db import migrations, models
import django.utils.timezone
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_auto_20190923_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='author',
            field=models.CharField(max_length=2000, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='skolko',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('До 200 000 руб', 'До 200 000 руб'), ('От 200 000 руб до 500 000 руб', 'От 200 000 руб до 500 000 руб'), ('От 500 000 руб до 1 000 000 руб', 'От 500 000 руб до 1 000 000 руб'), ('Более 1 000 000 руб', 'Более 1 000 000 руб'), ('Более 5 000 000 руб', 'Более 5 000 000 руб')], error_messages={'required': 'Обязательное поле.'}, help_text='Укажите пожалуйста приблизительный диапазон', max_length=116, verbose_name='Сколько всего Вы должны ?'),
        ),
    ]
