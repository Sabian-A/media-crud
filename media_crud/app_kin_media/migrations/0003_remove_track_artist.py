# Generated by Django 3.2 on 2022-06-15 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_kin_media', '0002_alter_album_album_genre_alter_album_artist_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='artist',
        ),
    ]