# Generated by Django 3.0.7 on 2020-06-20 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_text', models.CharField(max_length=200)),
                ('content_text', models.CharField(max_length=100000)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
