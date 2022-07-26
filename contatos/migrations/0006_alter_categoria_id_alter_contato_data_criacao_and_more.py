# Generated by Django 4.0.5 on 2022-07-21 03:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0005_alter_categoria_id_alter_contato_data_criacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='data_criacao',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='contato',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='nome',
            field=models.CharField(max_length=150),
        ),
    ]
