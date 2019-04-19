# Generated by Django 2.2 on 2019-04-19 06:47

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True)),
                ('year', models.PositiveSmallIntegerField()),
                ('race_name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('horses', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('category', models.CharField(blank=True, choices=[('PastPre', "Past Years' Triple Crown Prep Races"), ('PastTCR', "Past Years' Triple Crown Races"), ('TCR', "This Year's Triple Crown Races"), ('Pre', "Races Leading Up To This Year's Triple Crown")], max_length=4)),
                ('results', django.contrib.postgres.fields.jsonb.JSONField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Horse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('age', models.PositiveSmallIntegerField()),
                ('owner', models.CharField(max_length=200)),
                ('sire', models.CharField(max_length=200)),
                ('dam', models.CharField(max_length=200)),
                ('career_winnings', models.PositiveIntegerField()),
                ('career_wins', models.PositiveSmallIntegerField()),
                ('career_places', models.PositiveSmallIntegerField()),
                ('career_shows', models.PositiveSmallIntegerField()),
                ('breed', models.CharField(max_length=50)),
                ('races', models.ManyToManyField(to='jsonapi.Race')),
            ],
        ),
    ]