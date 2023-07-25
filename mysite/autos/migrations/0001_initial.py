# Generated by Django 4.0.7 on 2023-07-24 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=300)),
                ('mileage', models.IntegerField(null=True)),
                ('comments', models.TextField(default='')),
                ('make', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='autos.make')),
            ],
        ),
    ]
