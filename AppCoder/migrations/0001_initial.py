# Generated by Django 4.0.4 on 2022-04-21 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('parentesco', models.CharField(max_length=20)),
                ('edad', models.IntegerField()),
                ('directo', models.BooleanField()),
            ],
        ),
    ]