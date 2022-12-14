# Generated by Django 4.1.3 on 2022-11-27 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_petition_status_citizen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citizen',
            name='number',
        ),
        migrations.AlterField(
            model_name='petition',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='petition',
            name='status',
            field=models.CharField(choices=[('cur', 'Сбор подписей'), ('viw', 'На рассмотрении'), ('res', 'Готов ответ')], default='cur', max_length=3),
        ),
    ]
