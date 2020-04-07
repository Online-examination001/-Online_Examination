# Generated by Django 3.0.4 on 2020-04-07 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('university_name', models.CharField(max_length=225, verbose_name=' University name')),
                ('university_abb', models.CharField(max_length=20, unique=True, verbose_name=' University Abbreviation')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name=' username')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date joined')),
                ('date_login', models.DateTimeField(auto_now=True, verbose_name='date login')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_super', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
