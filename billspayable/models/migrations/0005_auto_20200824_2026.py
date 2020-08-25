# Generated by Django 2.2 on 2020-08-24 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0004_auto_20200824_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='invoice_id',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.IntegerField(choices=[(2, 'Approved'), (3, 'Rejected'), (4, 'Edited and approved'), (1, 'Pending')], default=1),
        ),
    ]