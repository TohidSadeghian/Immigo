# Generated by Django 4.1.3 on 2022-12-05 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0003_alter_news_date_published_alter_news_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
