# Generated by Django 3.0.3 on 2020-03-12 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0012_auto_20200312_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='topic_item',
            name='more',
            field=models.TextField(max_length=1000),
        ),
    ]