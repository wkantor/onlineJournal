# Generated by Django 3.0.3 on 2020-03-16 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0015_auto_20200316_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic_item',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]