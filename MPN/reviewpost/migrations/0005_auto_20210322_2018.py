# Generated by Django 3.1.7 on 2021-03-22 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewpost', '0004_auto_20210322_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewpost',
            name='photos',
            field=models.ImageField(blank=True, default='p1.png', null=True, upload_to=''),
        ),
    ]
