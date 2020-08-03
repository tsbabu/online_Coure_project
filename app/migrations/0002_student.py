# Generated by Django 2.2.1 on 2020-07-15 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=64)),
                ('contact_no', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.IntegerField()),
            ],
        ),
    ]