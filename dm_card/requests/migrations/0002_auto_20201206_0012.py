# Generated by Django 3.1.4 on 2020-12-06 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='is_approved',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='request',
            name='limit_credit',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='request',
            name='monthly_income',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request',
            name='score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
