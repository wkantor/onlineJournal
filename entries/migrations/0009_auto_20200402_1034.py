# Generated by Django 3.0.3 on 2020-04-02 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0008_entry_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='topic',
            field=models.TextField(),
        ),
    ]
