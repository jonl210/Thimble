# Generated by Django 3.1.5 on 2021-05-08 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210508_2244'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkPost',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='posts.post')),
                ('link', models.URLField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('posts.post',),
        ),
    ]