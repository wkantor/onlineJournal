# Generated by Django 3.0.3 on 2020-04-02 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0007_auto_20200331_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='topic',
            field=models.TextField(null=True),
        ),
    ]