# Generated by Django 4.0.4 on 2022-08-24 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_news_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(default='Категория не выбрана', on_delete=django.db.models.deletion.PROTECT, to='news.category'),
        ),
    ]