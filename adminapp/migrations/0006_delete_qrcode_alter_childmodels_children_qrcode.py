# Generated by Django 4.1.4 on 2022-12-14 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_qrcode_remove_childmodels_url'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QrCode',
        ),
        migrations.AlterField(
            model_name='childmodels',
            name='children_qrcode',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
