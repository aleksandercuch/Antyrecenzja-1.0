# Generated by Django 2.0.13 on 2019-03-11 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190311_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='writer',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
