# Generated by Django 3.0.2 on 2020-01-21 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=13)),
                ('timestamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
