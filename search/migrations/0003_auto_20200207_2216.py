# Generated by Django 3.0.2 on 2020-02-07 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prof',
            name='category',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='prof',
            name='name',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]
