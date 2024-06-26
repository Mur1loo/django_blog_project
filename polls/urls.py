from django.urls import path
from . import views

urlpatterns = [
    path("<int:question_id>/vote/", views.vote, name="vote"), #ex: /polls/5/vote
    path("<int:question_id>/", views.details, name="details"), #ex: /polls/5/
    path("<int:question_id>/results/", views.results, name="results"), #ex: /polls/5/results
    path("", views.index, name="index")
]
