# Generated by Django 2.1.5 on 2019-11-14 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbapp', '0002_auto_20191114_1811'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created']},
        ),
    ]