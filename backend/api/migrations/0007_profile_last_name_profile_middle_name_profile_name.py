# Generated by Django 4.2.11 on 2024-04-27 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_teammember_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='middle_name',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
