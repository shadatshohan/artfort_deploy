# Generated by Django 3.1 on 2022-02-21 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('keyword', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='icon/')),
                ('phone', models.IntegerField()),
                ('banner_bottom', models.ImageField(upload_to='settings/')),
                ('schedule_bottom', models.ImageField(upload_to='settings/')),
                ('trending1', models.ImageField(upload_to='settings/')),
                ('trending2', models.ImageField(upload_to='settings/')),
                ('trending3', models.ImageField(upload_to='settings/')),
                ('banner_last1', models.ImageField(upload_to='settings/')),
                ('banner_last2', models.ImageField(upload_to='settings/')),
                ('fax', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('smptserver', models.CharField(blank=True, max_length=100)),
                ('smtpemail', models.EmailField(blank=True, max_length=50, null=True)),
                ('smptpassword', models.CharField(blank=True, max_length=50)),
                ('smptport', models.CharField(blank=True, max_length=100)),
                ('facebook', models.CharField(blank=True, max_length=100)),
                ('instagram', models.CharField(blank=True, max_length=100)),
                ('address', models.TextField()),
                ('status', models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
