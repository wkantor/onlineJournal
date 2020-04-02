# Generated by Django 3.0.3 on 2020-03-30 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0003_topic_item2'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic_item2',
            options={'verbose_name_plural': 'Topic_items2'},
        ),
        migrations.AddField(
            model_name='question',
            name='comment',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='quote',
            name='comment',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='quote_item',
            name='comment',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='shadow',
            name='comment',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='shadow_item',
            name='comment',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='comment',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='topic_item',
            name='comment',
            field=models.TextField(max_length=2000, null=True),
        ),
    ]