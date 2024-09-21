# Generated by Django 4.1.1 on 2022-12-13 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_alter_childmodels_children_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='childmodels',
            name='url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='childmodels',
            name='children_qrcode',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
