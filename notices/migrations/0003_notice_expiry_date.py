# Generated by Django 5.1.2 on 2024-11-11 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0002_notice_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='expiry_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
