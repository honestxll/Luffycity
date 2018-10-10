# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-06 05:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('api', '0003_coupon_couponrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.SmallIntegerField(choices=[(0, '微信'), (1, '支付宝'), (2, '优惠码'), (3, '贝里')])),
                ('payment_number', models.CharField(blank=True, max_length=128, null=True, verbose_name='支付宝第三方订单号')),
                ('order_number', models.CharField(max_length=128, unique=True, verbose_name='订单号')),
                ('actual_amount', models.FloatField(verbose_name='实际支付金额')),
                ('status', models.SmallIntegerField(choices=[(0, '交易成功'), (1, '待支付'), (2, '退费申请中'), (3, '已退费'), (4, '主动取消'), (5, '超时取消')], verbose_name='交易状态')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='订单生成时间')),
                ('pay_time', models.DateTimeField(blank=True, null=True, verbose_name='订单付款时间')),
                ('cancel_time', models.DateTimeField(blank=True, null=True, verbose_name='订单取消时间')),
            ],
            options={
                'verbose_name': '订单表',
                'verbose_name_plural': '订单表',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_price', models.FloatField(verbose_name='课程原价')),
                ('price', models.FloatField(verbose_name='折后价格')),
                ('valid_period_display', models.CharField(max_length=32, verbose_name='有效期显示')),
                ('valid_period', models.PositiveIntegerField(verbose_name='有效期（days）')),
                ('content', models.CharField(blank=True, max_length=255, null=True)),
                ('memo', models.CharField(blank=True, max_length=255, null=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Order')),
            ],
            options={
                'verbose_name': '订单详情',
                'verbose_name_plural': '订单详情',
            },
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户表', 'verbose_name_plural': '用户表'},
        ),
        migrations.AlterModelOptions(
            name='usertoken',
            options={'verbose_name': '用户Token表', 'verbose_name_plural': '用户Token表'},
        ),
        migrations.AlterField(
            model_name='coupon',
            name='money_equivalent_value',
            field=models.IntegerField(blank=True, default=0, verbose_name='等值货币'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User'),
        ),
        migrations.AlterUniqueTogether(
            name='orderdetail',
            unique_together=set([('order', 'content_type', 'object_id')]),
        ),
    ]
