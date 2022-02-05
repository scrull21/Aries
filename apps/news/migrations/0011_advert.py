# Generated by Django 3.2.7 on 2022-02-05 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_newscomment_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='add_image/')),
            ],
            options={
                'verbose_name': 'Реклама',
            },
        ),
    ]