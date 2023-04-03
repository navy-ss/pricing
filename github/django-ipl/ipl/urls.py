from django.urls import path
from . import views

app_name = 'ipl'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/matches_per_year/', views.matches_per_year, name='matches_per_year'),
    path('api/wins_per_team_per_year/', views.wins_per_team_per_year, name='wins_per_team_per_year'),
    path('api/extra_runs_conceded_2016/', views.extra_runs_conceded_2016, name='extra_runs_conceded_2016'),
    path('api/top_economical_bowlers_2015/', views.top_economical_bowlers_2015, name='top_economical_bowlers_2015'),

    path('matches_per_year_chart/', views.matches_per_year_chart, name='matches_per_year_chart'),
    path('wins_per_team_per_year_chart/', views.wins_per_team_per_year_chart, name='wins_per_team_per_year_chart'),
    path('extra_runs_conceded_2016_chart/', views.extra_runs_conceded_2016_chart,
         name='extra_runs_conceded_2016_chart'),
    path('top_economical_bowlers_2015_chart/', views.top_economical_bowlers_2015_chart,
         name='top_economical_bowlers_2015_chart'),
]
