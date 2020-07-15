# Generated by Django 3.0.8 on 2020-07-15 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KnotEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_text', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('content_text', models.TextField()),
                ('comic_image', models.ImageField(upload_to='kotw')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
    ]
