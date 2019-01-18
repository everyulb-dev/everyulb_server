# Generated by Django 2.0.2 on 2019-01-18 10:54

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('is_milestone', models.BooleanField(default=False)),
                ('amount_allocated', models.IntegerField(default=0, help_text='Add in Paisa')),
                ('amount_used', models.IntegerField(default=0, help_text='Add in Paisa')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('status', models.CharField(choices=[('planning', 'Planning'), ('execution', 'Execution'), ('impact', 'Impact')], default='planning', max_length=50)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.Report')),
            ],
        ),
    ]
