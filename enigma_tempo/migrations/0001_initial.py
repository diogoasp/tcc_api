# Generated by Django 4.1.2 on 2022-10-14 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Nome')),
                ('cost', models.IntegerField(verbose_name='Custo')),
                ('hp', models.IntegerField(verbose_name='Vida')),
                ('atk', models.IntegerField(verbose_name='Ataque')),
                ('lore', models.TextField(verbose_name='História')),
                ('img', models.TextField(verbose_name='Arte')),
            ],
        ),
    ]
