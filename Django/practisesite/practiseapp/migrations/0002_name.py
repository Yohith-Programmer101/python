# Generated by Django 3.1.1 on 2021-01-04 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practiseapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
            ],
        ),
    ]
