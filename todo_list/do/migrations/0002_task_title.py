# Generated by Django 4.1.7 on 2023-03-13 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('do', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.CharField(default='ddff', max_length=50),
            preserve_default=False,
        ),
    ]
