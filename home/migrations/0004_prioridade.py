# Generated by Django 4.0.1 on 2022-03-16 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_tipoordem'),
    ]

    operations = [
        migrations.CreateModel(
            name='prioridade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomePrioridade', models.CharField(max_length=20)),
            ],
        ),
    ]