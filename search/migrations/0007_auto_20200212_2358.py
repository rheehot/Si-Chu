# Generated by Django 3.0.2 on 2020-02-12 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_auto_20200210_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='icon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='icons', to='search.Icon'),
        ),
        migrations.AlterField(
            model_name='icon',
            name='category',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='icon',
            name='tag',
            field=models.CharField(max_length=100),
        ),
    ]
