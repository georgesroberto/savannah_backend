# Generated by Django 5.1.1 on 2024-09-16 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(default='0796807438', max_length=15),
            preserve_default=False,
        ),
    ]
