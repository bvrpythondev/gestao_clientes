# Generated by Django 2.2.1 on 2019-06-30 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0003_auto_20190621_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='numero',
            field=models.CharField(max_length=8),
        ),
    ]
