# Generated by Django 3.1 on 2022-02-21 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0005_auto_20220221_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerimages',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
