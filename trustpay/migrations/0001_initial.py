# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-10 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(blank=True, default=None, null=True, verbose_name='IP address')),
                ('params_get', models.TextField(verbose_name='GET params')),
                ('params_post', models.TextField(verbose_name='POST params')),
                ('aid', models.CharField(max_length=10, verbose_name='Merchant account ID')),
                ('type', models.CharField(choices=[('CRDT', 'Credit card'), ('DBIT', 'Debit')], max_length=4, verbose_name='Type of transaction')),
                ('amount', models.CharField(max_length=16, verbose_name='Amount of the payment')),
                ('currency', models.CharField(max_length=3, verbose_name='Currency of the payment')),
                ('reference', models.CharField(max_length=500, verbose_name='Reference')),
                ('result', models.CharField(choices=[('0', 'Success'), ('1', 'Pending'), ('2', 'Announced'), ('3', 'Authorized'), ('4', 'Processing'), ('5', 'Authorized only'), ('1001', 'Invalid request'), ('1002', 'Unknown account'), ('1003', 'Merchant account disabled'), ('1004', 'Invalid sign'), ('1005', 'User cancel'), ('1006', 'Invalid authentication'), ('1007', 'Disposable balance'), ('1008', 'Service not allowed'), ('1009', 'PaySafeCard timeout'), ('1100', 'General Error'), ('1101', 'Unsupported currency conversion')], max_length=32, verbose_name='Result')),
                ('signature', models.CharField(max_length=64, verbose_name='Signature')),
                ('transaction_id', models.CharField(max_length=10, verbose_name='TrustPay Transaction ID')),
                ('order_id', models.CharField(max_length=10, verbose_name='TrustPay Order ID')),
                ('is_test', models.BooleanField(verbose_name='test')),
                ('is_signed', models.BooleanField(verbose_name='signed')),
                ('is_safe', models.BooleanField(help_text='signed and correct signature', verbose_name='safe')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='created')),
            ],
            options={
                'verbose_name': 'notification',
                'verbose_name_plural': 'notifications',
                'ordering': ('-created',),
                'db_table': 'trustpay_notifications',
            },
        ),
    ]
