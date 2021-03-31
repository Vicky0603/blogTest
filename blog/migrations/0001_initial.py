# Generated by Django 3.0.5 on 2020-04-30 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
                ('featured_image', models.ImageField(upload_to='images/%Y/%m/')),
            ],
        ),
    ]
