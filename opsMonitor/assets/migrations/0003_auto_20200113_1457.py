# Generated by Django 2.2 on 2020-01-13 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_auto_20200109_1747'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assets',
            options={'verbose_name': '主机资产', 'verbose_name_plural': '主机资产'},
        ),
        migrations.AlterModelOptions(
            name='component',
            options={'verbose_name': '组件', 'verbose_name_plural': '组件'},
        ),
    ]