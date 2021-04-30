# Generated by Django 3.2 on 2021-04-30 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('topic', models.TextField()),
                ('writer', models.TextField()),
                ('parties', models.TextField()),
                ('meeting_date', models.DateTimeField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]