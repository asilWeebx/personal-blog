# Generated by Django 4.2.8 on 2023-12-28 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_emails_recipient'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='url',
            field=models.URLField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]
