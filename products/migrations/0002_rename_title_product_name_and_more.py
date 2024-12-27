# Generated by Django 5.1.4 on 2024-12-27 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="title",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="seller",
            new_name="owner",
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(blank=True),
        ),
    ]
