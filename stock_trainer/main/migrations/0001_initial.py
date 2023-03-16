# Generated by Django 4.1.1 on 2023-03-14 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название актива')),
                ('num', models.IntegerField(verbose_name='Кол-во')),
                ('price', models.IntegerField(verbose_name='Цена'))
            ],
            options={
                'verbose_name': 'Актив',
                'verbose_name_plural': 'Активы',
            },
        ),
    ]
