# Generated by Django 5.1.7 on 2025-04-04 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_colorscheme_id_alter_colorscheme_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='colorscheme',
            name='is_dark',
            field=models.BooleanField(default=True),
        ),
    ]
