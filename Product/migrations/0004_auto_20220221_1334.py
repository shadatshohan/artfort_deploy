# Generated by Django 3.1 on 2022-02-21 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_auto_20220221_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerimages',
            name='title',
            field=models.CharField(default='THE BIGGEST', max_length=200),
        ),
    ]
