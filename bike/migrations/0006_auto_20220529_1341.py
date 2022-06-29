# Generated by Django 3.1.2 on 2022-05-29 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0005_rename_descripciontipobicicleta_bicicleta_descripcionbicicleta_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bicicleta',
            name='imagen',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
        migrations.AlterField(
            model_name='bicicleta',
            name='idBicicleta',
            field=models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='Código'),
        ),
    ]
