# Generated by Django 3.1 on 2022-02-21 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_auto_20220221_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerimages',
            name='desc',
            field=models.TextField(default='Special For Today'),
        ),
        migrations.AlterField(
            model_name='bannerimages',
            name='title',
            field=models.CharField(default='THE BIGGEST SALE shohan', max_length=200),
        ),
    ]
