# Generated by Django 3.0.2 on 2020-01-09 10:00

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0003_auto_20200109_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monitortask',
            name='send_tool',
        ),
        migrations.AddField(
            model_name='monitortask',
            name='send_context',
            field=models.TextField(default=datetime.datetime(2020, 1, 9, 10, 0, 42, 556093, tzinfo=utc), verbose_name='发送内容'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='monitortask',
            name='send_tool_templates',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='monitor.MonitorTemplates', verbose_name='发送模板'),
            preserve_default=False,
        ),
    ]