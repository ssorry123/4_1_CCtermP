# Generated by Django 3.0.6 on 2020-06-22 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_chatting_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatting',
            name='member',
            field=models.CharField(max_length=1000, null=True, verbose_name='MEMBER'),
        ),
    ]
