# Generated by Django 5.0.6 on 2024-07-20 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='published_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
