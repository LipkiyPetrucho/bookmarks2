# Generated by Django 4.2.3 on 2024-02-20 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-created'], 'verbose_name': 'изображение', 'verbose_name_plural': 'изображений'},
        ),
    ]