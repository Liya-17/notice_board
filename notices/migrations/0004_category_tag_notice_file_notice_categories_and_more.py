# Generated by Django 5.1.2 on 2024-11-11 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0003_notice_expiry_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='notice',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='notices/'),
        ),
        migrations.AddField(
            model_name='notice',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='notices', to='notices.category'),
        ),
        migrations.AddField(
            model_name='notice',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='notices', to='notices.tag'),
        ),
    ]