# Generated by Django 3.0.3 on 2020-03-30 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0002_remove_entry_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic_item2',
            fields=[
                ('content', models.TextField(max_length=2000)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entries.Topic_item')),
            ],
        ),
    ]
