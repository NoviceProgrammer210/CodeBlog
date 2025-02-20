# Generated by Django 5.1.5 on 2025-01-19 09:48

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
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('slug', models.EmailField(max_length=30)),
                ('timestamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
