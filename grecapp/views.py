from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import JsonResponse
from django.contrib import messages
from .models import Operation, Agent, Cadastre, Titre, Indice, Quittance, Personne



def login_view(request):
    if request.method == "POST":
        login = request.POST.get("login")
        mdp = request.POST.get("mdp")

        try:
            agent = Agent.objects.get(login=login, mdp=mdp)
            request.session["agent_id"] = agent.idagent
            return redirect("encaissement")
        except Agent.DoesNotExist:
            messages.error(request, "Login ou mot de passe incorrect !")

    return render(request, "grecapp/login.html")

def encaissement(request):
    if "agent_id" not in request.session:
        return redirect("login")

    agent = Agent.objects.get(idagent=request.session["agent_id"])
    return render(request, "grecapp/encaissement.html", {"agent": agent})

