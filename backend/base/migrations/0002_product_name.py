# Generated by Django 3.1.6 on 2021-02-04 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='a', max_length=255),
            preserve_default=False,
        ),
    ]