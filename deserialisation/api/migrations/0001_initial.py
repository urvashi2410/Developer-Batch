# Generated by Django 4.0.4 on 2022-06-06 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('rollNo', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
            ],
        ),
    ]
