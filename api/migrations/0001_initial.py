# Generated by Django 2.2.10 on 2020-02-19 15:30

import api.models
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='姓名')),
                ('gender', models.CharField(choices=[('男', '男'), ('女', '女')], max_length=1, verbose_name='性别')),
                ('number', models.CharField(max_length=10, verbose_name='学号')),
                ('photo', models.ImageField(blank=True, max_length=256, upload_to=api.models.image_path, verbose_name='照片')),
                ('courses', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=api.models.get_default_json, verbose_name='课程')),
            ],
            options={
                'verbose_name': '学生',
                'verbose_name_plural': '学生',
                'ordering': ['id'],
            },
        ),
    ]
