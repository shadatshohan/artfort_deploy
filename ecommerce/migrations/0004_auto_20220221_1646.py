# Generated by Django 3.1 on 2022-02-21 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_auto_20220221_1641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setting',
            old_name='banner_bottom1',
            new_name='bannerbottom1',
        ),
        migrations.RenameField(
            model_name='setting',
            old_name='banner_bottom2',
            new_name='bannerbottom2',
        ),
        migrations.RenameField(
            model_name='setting',
            old_name='banner_last1',
            new_name='bannerlast1',
        ),
        migrations.RenameField(
            model_name='setting',
            old_name='banner_last2',
            new_name='bannerlast2',
        ),
        migrations.RenameField(
            model_name='setting',
            old_name='schedule_bottom',
            new_name='schedulebottom',
        ),
    ]