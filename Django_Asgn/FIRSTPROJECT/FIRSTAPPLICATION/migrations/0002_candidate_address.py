# Generated by Django 3.2.6 on 2021-08-15 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FIRSTAPPLICATION', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='address',
            field=models.CharField(default='not available', max_length=300),
        ),
    ]