# Generated by Django 4.1.4 on 2022-12-14 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QRModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qrcode', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
    ]
