# Generated by Django 3.2.5 on 2024-01-29 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0002_tournament_online'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='current_round',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='tournament',
            name='finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tournament',
            name='rounds',
            field=models.IntegerField(default=1),
        ),
        migrations.CreateModel(
            name='TournamentMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round', models.IntegerField(default=1)),
                ('match_id', models.IntegerField(default=1)),
                ('player1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player1', to='tournament.player')),
                ('player2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player2', to='tournament.player')),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='tournament.player')),
            ],
        ),
        migrations.AddField(
            model_name='tournament',
            name='matchs',
            field=models.ManyToManyField(blank=True, to='tournament.TournamentMatch'),
        ),
    ]
