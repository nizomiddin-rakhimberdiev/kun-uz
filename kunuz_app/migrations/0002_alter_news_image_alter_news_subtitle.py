# Generated by Django 5.0.4 on 2024-05-03 11:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kunuz_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="media/images/news-images/"
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="subtitle",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]