# Generated by Django 3.1.3 on 2021-06-20 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210620_1208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='contetn',
            new_name='content',
        ),
    ]
