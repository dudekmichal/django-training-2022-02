# from django.http import HttpResponse
from django.shortcuts import render
from .models import Person


def hello_world(request):
    biggest_debtor = Person.objects.order_by('-debt')[0]

    context = {"name": biggest_debtor.name,
               "age": biggest_debtor.age,
               "debt": biggest_debtor.debt}
    return render(request, template_name="competitor/hello.html", context=context)


def about(request):
    return render(request, template_name="competitor/about.html")


def prize(request):
    context = {"current_prize": Person.get_current_prize()}
    return render(request, template_name="competitor/prize.html", context=context)


def statistics(request):
    context = {"alive_competitors_count": Person.get_alive_competitors_count(),
               "all_competitors_count": Person.get_all_competitors_count(),
               "debt_summary": Person.get_debt_summary(),
               "current_prize": Person.get_current_prize(),
               "all_competitors": Person.get_all_competitors(),
               "all_alive_competitors": Person.get_alive_competitors()}

    return render(request, template_name="competitor/statistics.html", context=context)


def player_details(request, player_number):
    try:
        player = Person.get_player_by_id(player_number)
        context = {"id": player.id,
                   "name": player.name,
                   "debt": player.debt}
    except Person.DoesNotExist:
        context = {
            "id": "N/A",
            "name": "N/A",
            "debt": "N/A"}

    return render(request, template_name="competitor/player_details.html", context=context)
