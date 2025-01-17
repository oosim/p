# Generated by Django 4.2.16 on 2024-12-15 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tap", "0004_region_post_region"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="region",
        ),
        migrations.AddField(
            model_name="region",
            name="slug",
            field=models.SlugField(
                allow_unicode=True, default="default", max_length=200, unique=True
            ),
            preserve_default=False,
        ),
    ]
