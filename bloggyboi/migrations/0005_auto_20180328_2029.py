# Generated by Django 2.0.1 on 2018-03-29 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloggyboi', '0004_post_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='field',
            field=models.CharField(choices=[('Auth', 'author'), ('Title', 'title'), ('Text', 'text'), ('Created', 'created_date'), ('Published', 'published_date'), ('Num', 'number')], default='', max_length=25),
        ),
    ]
