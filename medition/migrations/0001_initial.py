# Generated by Django 3.2.6 on 2023-05-07 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meditions',
            fields=[
                ('MeditionId', models.AutoField(primary_key=True, serialize=False)),
                ('Ph', models.FloatField(max_length=10)),
                ('Voltage', models.FloatField(max_length=10)),
                ('Current', models.FloatField(max_length=20)),
            ],
        ),
    ]