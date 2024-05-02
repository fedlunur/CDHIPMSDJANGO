# Generated by Django 4.2.11 on 2024-04-28 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0006_remove_task_member_member_task_checklist_task_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task_member',
            name='assigned_to',
        ),
        migrations.CreateModel(
            name='TaskAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task_member')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'task_member')},
            },
        ),
        migrations.AddField(
            model_name='task_member',
            name='assigned_to',
            field=models.ManyToManyField(through='tasks.TaskAssignment', to=settings.AUTH_USER_MODEL),
        ),
    ]
