# Generated by Django 3.1.3 on 2020-12-11 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hod',
            name='dept',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]