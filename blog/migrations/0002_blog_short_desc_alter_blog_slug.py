# Generated by Django 5.1.2 on 2024-11-18 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='short_desc',
            field=models.CharField(default=2, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.CharField(default='', max_length=300),
        ),
    ]
