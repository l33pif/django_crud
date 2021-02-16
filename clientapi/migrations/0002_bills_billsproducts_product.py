# Generated by Django 3.1.6 on 2021-02-16 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cliets_id', models.IntegerField()),
                ('company_name', models.CharField(max_length=100)),
                ('nit', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BillsProducts',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('bill_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=150)),
                ('nit', models.CharField(max_length=50)),
                ('attribute', models.CharField(max_length=100)),
            ],
        ),
    ]
