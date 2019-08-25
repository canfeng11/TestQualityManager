# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('QualityManager', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={},
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='avit_img',
        ),
        migrations.AlterField(
            model_name='bugdetail',
            name='creat_user',
            field=models.ForeignKey(null=True, related_name='creat_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bugdetail',
            name='order_to',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bugdetail',
            name='pro',
            field=models.ForeignKey(null=True, related_name='pro', to='QualityManager.Project'),
        ),
        migrations.AlterField(
            model_name='bugdetail',
            name='ver',
            field=models.ForeignKey(null=True, related_name='ver', to='QualityManager.Version'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='nick_name',
            field=models.CharField(verbose_name='岗位名称', max_length=10, default='新用户'),
        ),
        migrations.AlterModelTable(
            name='bugdetail',
            table='BugDetail',
        ),
        migrations.AlterModelTable(
            name='project',
            table='Project',
        ),
        migrations.AlterModelTable(
            name='userinfo',
            table='UserInfo',
        ),
        migrations.AlterModelTable(
            name='version',
            table='Version',
        ),
    ]
