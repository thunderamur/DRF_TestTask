# Generated by Django 2.2.1 on 2019-05-21 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='EnterprisesGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Сеть предприятий',
                'verbose_name_plural': 'Сети предприятий',
            },
        ),
        migrations.AlterModelOptions(
            name='district',
            options={'verbose_name': 'Район', 'verbose_name_plural': 'Районы'},
        ),
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
    ]
