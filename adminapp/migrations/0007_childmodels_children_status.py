# Generated by Django 4.1.4 on 2022-12-14 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0006_delete_qrcode_alter_childmodels_children_qrcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='childmodels',
            name='children_status',
            field=models.CharField(help_text='children_status', max_length=50, null=True),
        ),
    ]
