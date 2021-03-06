# Generated by Django 2.2 on 2020-08-25 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0007_auto_20200824_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='tax_perc',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=19),
        ),
    ]
