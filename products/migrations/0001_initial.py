# Generated by Django 2.0.5 on 2018-06-28 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('qt', models.IntegerField()),
                ('image', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Drinks',
            },
        ),
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('qt', models.IntegerField()),
                ('image', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Foods',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField()),
                ('user_name', models.CharField(max_length=50)),
                ('user_email', models.CharField(max_length=50)),
                ('product_name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('qt', models.IntegerField()),
                ('image', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Orders',
            },
        ),
    ]
