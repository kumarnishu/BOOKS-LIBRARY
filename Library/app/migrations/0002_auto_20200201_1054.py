# Generated by Django 3.0.2 on 2020-02-01 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='due_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='issue_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]