# Generated by Django 3.0.3 on 2020-03-12 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0013_auto_20200312_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]