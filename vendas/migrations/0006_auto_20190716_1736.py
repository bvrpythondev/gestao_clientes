# Generated by Django 2.2.1 on 2019-07-16 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0005_auto_20190707_1459'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='venda',
            options={'permissions': (('set_nfe', 'Alterar o valor da NF-e'), ('permissao2', 'Permissao 2'), ('permissao3', 'Persmissao 3'))},
        ),
    ]
