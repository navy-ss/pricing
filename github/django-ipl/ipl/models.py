from django.db import models

# Create your models here.


class Match(models.Model):
    id = models.AutoField(primary_key=True)
    season = models.IntegerField()
    city = models.CharField(max_length=100, null=True)
    date = models.DateField()
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    toss_winner = models.CharField(max_length=100)
    toss_decision = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    dl_applied = models.IntegerField()  # 0 or 1
    winner = models.CharField(max_length=100, null=True)
    wins_by_runs = models.IntegerField()
    wins_by_wickets = models.IntegerField()
    player_of_match = models.CharField(max_length=100, null=True)
    venue = models.CharField(max_length=100)
    umpire1 = models.CharField(max_length=100, null=True)
    umpire2 = models.CharField(max_length=100, null=True)
    umpire3 = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.season


class Delivery(models.Model):
    id = models.AutoField(primary_key=True)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    inning = models.IntegerField()
    batting_team = models.CharField(max_length=100)
    bowling_team = models.CharField(max_length=100)
    over = models.IntegerField()
    ball = models.IntegerField()
    batsman = models.CharField(max_length=100)
    non_striker = models.CharField(max_length=100)
    bowler = models.CharField(max_length=100)
    is_super_over = models.IntegerField()  # 0 or 1
    wide_runs = models.IntegerField()
    bye_runs = models.IntegerField()
    legbye_runs = models.IntegerField()
    noball_runs = models.IntegerField()
    penalty_runs = models.IntegerField()
    batsman_runs = models.IntegerField()
    extra_runs = models.IntegerField()
    total_runs = models.IntegerField()
    player_dismissed = models.CharField(max_length=100, null=True)
    dismissal_kind = models.CharField(max_length=100, null=True)
    fielder = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.match
