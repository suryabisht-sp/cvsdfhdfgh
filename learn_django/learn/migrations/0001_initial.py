# Generated by Django 5.0.4 on 2024-05-03 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Myapp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('des', models.TextField()),
            ],
        ),
    ]