# Generated by Django 3.0.7 on 2020-06-20 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogentry',
            name='content_text',
            field=models.TextField(),
        ),
    ]
