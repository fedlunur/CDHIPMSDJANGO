# Generated by Django 4.2.11 on 2024-04-09 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_team_teammember_remove_teammembers_members'),
        ('tasks', '0005_task_card_cover_task_card_created_at_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TeamMembers',
        ),
        migrations.AddField(
            model_name='teammember',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.team'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.profile'),
        ),
        migrations.AlterUniqueTogether(
            name='teammember',
            unique_together={('user', 'team')},
        ),
    ]
