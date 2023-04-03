from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count, Sum
from ipl.models import Match, Delivery

# Create your views here.
# Number of matches played per year for all the years in IPL.


def index(request):
    return render(request, 'index.html')


def matches_per_year(request):
    result = Match.objects.values('season').annotate(matches=Count('id')).order_by('season')
    return JsonResponse(list(result), safe=False)


def wins_per_team_per_year(request):
    matches = Match.objects.values('season', 'winner').exclude(winner='').annotate(
        wins=Count('winner')).order_by('season')

    wins_per_team = {}
    for match in matches:
        season = match['season']
        team = match['winner']
        wins = match['wins']

        if season not in wins_per_team:
            wins_per_team[season] = {}

        wins_per_team[season][team] = wins

    return JsonResponse(wins_per_team, safe=False)


def extra_runs_conceded_2016(request):
    result = Delivery.objects.filter(match__season=2016).values('bowling_team').annotate(
        extra_runs_conceded=Sum('extra_runs')).order_by('bowling_team')
    return JsonResponse(list(result), safe=False)

# def extra_runs_conceded_2016(request):
#     deliveries = Delivery.objects.filter(match__season=2016).values('bowling_team').annotate(
#       extra_runs=Sum('extra_runs'))
#     extra_runs = {}
#     for delivery in deliveries:
#         team = delivery['bowling_team']
#         runs = delivery['extra_runs']
#         extra_runs[team] = runs

#     return JsonResponse(extra_runs, safe=False)


# def top_economical_bowlers_2015(request):
#     bowler_stats = Delivery.objects.filter(match__season=2015).values('bowler').annotate(
#         total_runs=Sum('total_runs'),
#         balls=Count('id'),
#         overs=Count('id') / 6,
#         extra_balls=Count('id') % 6,
#     )

#     for stats in bowler_stats:
#         stats['economy'] = stats['total_runs'] / (stats['overs'] + stats['extra_balls'] / 6)

#     bowler_stats = sorted(bowler_stats, key=lambda stats: stats['economy'])[:10]
#     return JsonResponse(bowler_stats, safe=False)


def top_economical_bowlers_2015(request):
    deliveries = Delivery.objects.filter(match__season=2015).values('bowler').annotate(
        runs=Sum('total_runs') - Sum('bye_runs') - Sum('legbye_runs'),
        balls=Count('ball') - (Count('ball') % 6)).order_by('runs', 'balls')

    bowlers = {}
    for delivery in deliveries:
        bowler = delivery['bowler']
        runs = delivery['runs']
        balls = delivery['balls']
        economy = round(runs / balls * 6, 2)
        bowlers[bowler] = economy

    # top 10 bowlers
    bowlers = dict(sorted(bowlers.items(), key=lambda item: item[1])[:10])
    return JsonResponse(bowlers, safe=False)


def matches_per_year_chart(request):
    return render(request, 'matches_per_year_chart.html')


def wins_per_team_per_year_chart(request):
    return render(request, 'wins_per_team_per_year_chart.html')


def extra_runs_conceded_2016_chart(request):
    return render(request, 'extra_runs_conceded_2016_chart.html')


def top_economical_bowlers_2015_chart(request):
    return render(request, 'top_economical_bowlers_2015_chart.html')
