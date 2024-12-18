# Generated by Django 5.1.4 on 2024-12-18 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sprite', models.URLField()),
                ('types', models.CharField(max_length=100)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
            ],
        ),
    ]
