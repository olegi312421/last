# Generated by Django 4.1.6 on 2023-02-18 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50, unique=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('position', models.SmallIntegerField(unique=True)),
                ('about', models.CharField(max_length=255)),
            ],
        ),
    ]
