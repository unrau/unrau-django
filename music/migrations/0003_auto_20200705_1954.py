# Generated by Django 3.0.8 on 2020-07-05 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_musicentry_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicentry',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
    ]
