from django.core.management.base import BaseCommand
from django.db import transaction
from ipl.models import Match, Delivery
import csv


class Command(BaseCommand):
    help = 'Import IPL dataset into the database'

    def handle(self, *args, **options):
        # Import data using atomic transactions
        with transaction.atomic():
            # Import match data
            with open('matches.csv', 'r', encoding='utf-8') as matches_file:
                matches_reader = csv.DictReader(matches_file)
                for row in matches_reader:
                    match = Match(
                        id=row['id'],
                        season=row['season'],
                        city=row['city'],
                        date=row['date'],
                        team1=row['team1'],
                        team2=row['team2'],
                        toss_winner=row['toss_winner'],
                        toss_decision=row['toss_decision'],
                        result=row['result'],
                        dl_applied=row['dl_applied'],  # == '1'
                        winner=row['winner'],
                        wins_by_runs=row['win_by_runs'],
                        wins_by_wickets=row['win_by_wickets'],
                        player_of_match=row['player_of_match'],
                        venue=row['venue'],
                        umpire1=row['umpire1'],
                        umpire2=row['umpire2'],
                        umpire3=row['umpire3'],
                    )
                    match.save()

            # Import delivery data
            with open('deliveries.csv', 'r', encoding='utf-8') as deliveries_file:
                deliveries_reader = csv.DictReader(deliveries_file)
                for row in deliveries_reader:
                    delivery = Delivery(
                        match_id=row['match_id'],
                        inning=row['inning'],
                        batting_team=row['batting_team'],
                        bowling_team=row['bowling_team'],
                        over=row['over'],
                        ball=row['ball'],
                        batsman=row['batsman'],
                        non_striker=row['non_striker'],
                        bowler=row['bowler'],
                        is_super_over=row['is_super_over'],  # == '1'
                        wide_runs=row['wide_runs'],
                        bye_runs=row['bye_runs'],
                        legbye_runs=row['legbye_runs'],
                        noball_runs=row['noball_runs'],
                        penalty_runs=row['penalty_runs'],
                        batsman_runs=row['batsman_runs'],
                        extra_runs=row['extra_runs'],
                        total_runs=row['total_runs'],
                        player_dismissed=row['player_dismissed'],
                        dismissal_kind=row['dismissal_kind'],
                        fielder=row['fielder'],
                    )
                    delivery.save()

        self.stdout.write(self.style.SUCCESS('Successfully imported IPL dataset'))
