# Generated by Django 3.0.2 on 2020-02-03 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200202_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(blank=True, default='none.jpg', null=True, upload_to='profile'),
        ),
    ]
