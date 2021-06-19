# Generated by Django 3.2.4 on 2021-06-19 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Window',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('main_category', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='main_category', to='home.category')),
                ('sub_category', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='sub_category', to='home.category')),
            ],
        ),
    ]
