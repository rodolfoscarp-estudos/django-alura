# Generated by Django 2.2.6 on 2022-05-27 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0004_receita_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='foto_receita',
            field=models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y/'),
        ),
    ]
