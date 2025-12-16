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



# app/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *

# ------------------------------
# TYPEAGENT
# ------------------------------
class TypeAgentListView(ListView):
    model = TypeAgent
    template_name = "typeagent_list.html"

class TypeAgentDetailView(DetailView):
    model = TypeAgent
    template_name = "typeagent_detail.html"

class TypeAgentCreateView(CreateView):
    model = TypeAgent
    form_class = TypeAgentForm
    template_name = "typeagent_form.html"
    success_url = reverse_lazy("typeagent_list")

class TypeAgentUpdateView(UpdateView):
    model = TypeAgent
    form_class = TypeAgentForm
    template_name = "typeagent_form.html"
    success_url = reverse_lazy("typeagent_list")

class TypeAgentDeleteView(DeleteView):
    model = TypeAgent
    template_name = "typeagent_confirm_delete.html"
    success_url = reverse_lazy("typeagent_list")


# ------------------------------
# TOPODOM
# ------------------------------
class TopoDomListView(ListView):
    model = TopoDom
    template_name = "topodom_list.html"

class TopoDomDetailView(DetailView):
    model = TopoDom
    template_name = "topodom_detail.html"

class TopoDomCreateView(CreateView):
    model = TopoDom
    form_class = TopoDomForm
    template_name = "topodom_form.html"
    success_url = reverse_lazy("topodom_list")

class TopoDomUpdateView(UpdateView):
    model = TopoDom
    form_class = TopoDomForm
    template_name = "topodom_form.html"
    success_url = reverse_lazy("topodom_list")

class TopoDomDeleteView(DeleteView):
    model = TopoDom
    template_name = "topodom_confirm_delete.html"
    success_url = reverse_lazy("topodom_list")


# ------------------------------
# ENTITE
# ------------------------------
class EntiteListView(ListView):
    model = Entite
    template_name = "entite_list.html"

class EntiteDetailView(DetailView):
    model = Entite
    template_name = "entite_detail.html"

class EntiteCreateView(CreateView):
    model = Entite
    form_class = EntiteForm
    template_name = "entite_form.html"
    success_url = reverse_lazy("entite_list")

class EntiteUpdateView(UpdateView):
    model = Entite
    form_class = EntiteForm
    template_name = "entite_form.html"
    success_url = reverse_lazy("entite_list")

class EntiteDeleteView(DeleteView):
    model = Entite
    template_name = "entite_confirm_delete.html"
    success_url = reverse_lazy("entite_list")


# ------------------------------
# AGENT
# ------------------------------
class AgentListView(ListView):
    model = Agent
    template_name = "agent_list.html"

class AgentDetailView(DetailView):
    model = Agent
    template_name = "agent_detail.html"

class AgentCreateView(CreateView):
    model = Agent
    form_class = AgentForm
    template_name = "agent_form.html"
    success_url = reverse_lazy("agent_list")

class AgentUpdateView(UpdateView):
    model = Agent
    form_class = AgentForm
    template_name = "agent_form.html"
    success_url = reverse_lazy("agent_list")

class AgentDeleteView(DeleteView):
    model = Agent
    template_name = "agent_confirm_delete.html"
    success_url = reverse_lazy("agent_list")


# ------------------------------
# CADASTRE
# ------------------------------
class CadastreListView(ListView):
    model = Cadastre
    template_name = "cadastre_list.html"

class CadastreDetailView(DetailView):
    model = Cadastre
    template_name = "cadastre_detail.html"

class CadastreCreateView(CreateView):
    model = Cadastre
    form_class = CadastreForm
    template_name = "cadastre_form.html"
    success_url = reverse_lazy("cadastre_list")

class CadastreUpdateView(UpdateView):
    model = Cadastre
    form_class = CadastreForm
    template_name = "cadastre_form.html"
    success_url = reverse_lazy("cadastre_list")

class CadastreDeleteView(DeleteView):
    model = Cadastre
    template_name = "cadastre_confirm_delete.html"
    success_url = reverse_lazy("cadastre_list")


# ------------------------------
# INDICE
# ------------------------------
class IndiceListView(ListView):
    model = Indice
    template_name = "indice_list.html"

class IndiceDetailView(DetailView):
    model = Indice
    template_name = "indice_detail.html"

class IndiceCreateView(CreateView):
    model = Indice
    form_class = IndiceForm
    template_name = "indice_form.html"
    success_url = reverse_lazy("indice_list")

class IndiceUpdateView(UpdateView):
    model = Indice
    form_class = IndiceForm
    template_name = "indice_form.html"
    success_url = reverse_lazy("indice_list")

class IndiceDeleteView(DeleteView):
    model = Indice
    template_name = "indice_confirm_delete.html"
    success_url = reverse_lazy("indice_list")


# ------------------------------
# PERSONNE
# ------------------------------
class PersonneListView(ListView):
    model = Personne
    template_name = "personne_list.html"

class PersonneDetailView(DetailView):
    model = Personne
    template_name = "personne_detail.html"

class PersonneCreateView(CreateView):
    model = Personne
    form_class = PersonneForm
    template_name = "personne_form.html"
    success_url = reverse_lazy("personne_list")

class PersonneUpdateView(UpdateView):
    model = Personne
    form_class = PersonneForm
    template_name = "personne_form.html"
    success_url = reverse_lazy("personne_list")

class PersonneDeleteView(DeleteView):
    model = Personne
    template_name = "personne_confirm_delete.html"
    success_url = reverse_lazy("personne_list")


# ------------------------------
# TYPEOPERATION
# ------------------------------
class TypeOperationListView(ListView):
    model = TypeOperation
    template_name = "typeoperation_list.html"

class TypeOperationDetailView(DetailView):
    model = TypeOperation
    template_name = "typeoperation_detail.html"

class TypeOperationCreateView(CreateView):
    model = TypeOperation
    form_class = TypeOperationForm
    template_name = "typeoperation_form.html"
    success_url = reverse_lazy("typeoperation_list")

class TypeOperationUpdateView(UpdateView):
    model = TypeOperation
    form_class = TypeOperationForm
    template_name = "typeoperation_form.html"
    success_url = reverse_lazy("typeoperation_list")

class TypeOperationDeleteView(DeleteView):
    model = TypeOperation
    template_name = "typeoperation_confirm_delete.html"
    success_url = reverse_lazy("typeoperation_list")


# ------------------------------
# OPERATION
# ------------------------------
class OperationListView(ListView):
    model = Operation
    template_name = "operation_list.html"

class OperationDetailView(DetailView):
    model = Operation
    template_name = "operation_detail.html"

class OperationCreateView(CreateView):
    model = Operation
    form_class = OperationForm
    template_name = "operation_form.html"
    success_url = reverse_lazy("operation_list")

class OperationUpdateView(UpdateView):
    model = Operation
    form_class = OperationForm
    template_name = "operation_form.html"
    success_url = reverse_lazy("operation_list")

class OperationDeleteView(DeleteView):
    model = Operation
    template_name = "operation_confirm_delete.html"
    success_url = reverse_lazy("operation_list")


# ------------------------------
# AVISPAYEMENT
# ------------------------------
class AvisPayementListView(ListView):
    model = AvisPayement
    template_name = "avispayement_list.html"

class AvisPayementDetailView(DetailView):
    model = AvisPayement
    template_name = "avispayement_detail.html"

class AvisPayementCreateView(CreateView):
    model = AvisPayement
    form_class = AvisPayementForm
    template_name = "avispayement_form.html"
    success_url = reverse_lazy("avispayement_list")

class AvisPayementUpdateView(UpdateView):
    model = AvisPayement
    form_class = AvisPayementForm
    template_name = "avispayement_form.html"
    success_url = reverse_lazy("avispayement_list")

class AvisPayementDeleteView(DeleteView):
    model = AvisPayement
    template_name = "avispayement_confirm_delete.html"
    success_url = reverse_lazy("avispayement_list")


# ------------------------------
# QUITTANCE
# ------------------------------
class QuittanceListView(ListView):
    model = Quittance
    template_name = "quittance_list.html"

class QuittanceDetailView(DetailView):
    model = Quittance
    template_name = "quittance_detail.html"

class QuittanceCreateView(CreateView):
    model = Quittance
    form_class = QuittanceForm
    template_name = "quittance_form.html"
    success_url = reverse_lazy("quittance_list")


    # ------------------------------
# QUITTANCE (suite)
# ------------------------------
class QuittanceUpdateView(UpdateView):
    model = Quittance
    form_class = QuittanceForm
    template_name = "quittance_form.html"
    success_url = reverse_lazy("quittance_list")

class QuittanceDeleteView(DeleteView):
    model = Quittance
    template_name = "quittance_confirm_delete.html"
    success_url = reverse_lazy("quittance_list")


# ------------------------------
# QUICADASTRE
# ------------------------------
class QuiCadastreListView(ListView):
    model = QuiCadastre
    template_name = "quicadastre_list.html"

class QuiCadastreDetailView(DetailView):
    model = QuiCadastre
    template_name = "quicadastre_detail.html"

class QuiCadastreCreateView(CreateView):
    model = QuiCadastre
    form_class = QuiCadastreForm
    template_name = "quicadastre_form.html"
    success_url = reverse_lazy("quicadastre_list")

class QuiCadastreUpdateView(UpdateView):
    model = QuiCadastre
    form_class = QuiCadastreForm
    template_name = "quicadastre_form.html"
    success_url = reverse_lazy("quicadastre_list")

class QuiCadastreDeleteView(DeleteView):
    model = QuiCadastre
    template_name = "quicadastre_confirm_delete.html"
    success_url = reverse_lazy("quicadastre_list")


# ------------------------------
# OPQUITTANCE
# ------------------------------
class OpQuittanceListView(ListView):
    model = OpQuittance
    template_name = "opquittance_list.html"

class OpQuittanceDetailView(DetailView):
    model = OpQuittance
    template_name = "opquittance_detail.html"

class OpQuittanceCreateView(CreateView):
    model = OpQuittance
    form_class = OpQuittanceForm
    template_name = "opquittance_form.html"
    success_url = reverse_lazy("opquittance_list")

class OpQuittanceUpdateView(UpdateView):
    model = OpQuittance
    form_class = OpQuittanceForm
    template_name = "opquittance_form.html"
    success_url = reverse_lazy("opquittance_list")

class OpQuittanceDeleteView(DeleteView):
    model = OpQuittance
    template_name = "opquittance_confirm_delete.html"
    success_url = reverse_lazy("opquittance_list")


# ------------------------------
# QUITTANCEPERSONNE
# ------------------------------
class QuittancePersonneListView(ListView):
    model = QuittancePersonne
    template_name = "quittancepersonne_list.html"

class QuittancePersonneDetailView(DetailView):
    model = QuittancePersonne
    template_name = "quittancepersonne_detail.html"

class QuittancePersonneCreateView(CreateView):
    model = QuittancePersonne
    form_class = QuittancePersonneForm
    template_name = "quittancepersonne_form.html"
    success_url = reverse_lazy("quittancepersonne_list")

class QuittancePersonneUpdateView(UpdateView):
    model = QuittancePersonne
    form_class = QuittancePersonneForm
    template_name = "quittancepersonne_form.html"
    success_url = reverse_lazy("quittancepersonne_list")

class QuittancePersonneDeleteView(DeleteView):
    model = QuittancePersonne
    template_name = "quittancepersonne_confirm_delete.html"
    success_url = reverse_lazy("quittancepersonne_list")


# ------------------------------
# TITRE
# ------------------------------
class TitreListView(ListView):
    model = Titre
    template_name = "titre_list.html"

class TitreDetailView(DetailView):
    model = Titre
    template_name = "titre_detail.html"

class TitreCreateView(CreateView):
    model = Titre
    form_class = TitreForm
    template_name = "titre_form.html"
    success_url = reverse_lazy("titre_list")

class TitreUpdateView(UpdateView):
    model = Titre
    form_class = TitreForm
    template_name = "titre_form.html"
    success_url = reverse_lazy("titre_list")

class TitreDeleteView(DeleteView):
    model = Titre
    template_name = "titre_confirm_delete.html"
    success_url = reverse_lazy("titre_list")


# ------------------------------
# QUITITRE
# ------------------------------
class QuiTitreListView(ListView):
    model = QuiTitre
    template_name = "quititre_list.html"

class QuiTitreDetailView(DetailView):
    model = QuiTitre
    template_name = "quititre_detail.html"

class QuiTitreCreateView(CreateView):
    model = QuiTitre
    form_class = QuiTitreForm
    template_name = "quititre_form.html"
    success_url = reverse_lazy("quititre_list")

class QuiTitreUpdateView(UpdateView):
    model = QuiTitre
    form_class = QuiTitreForm
    template_name = "quititre_form.html"
    success_url = reverse_lazy("quititre_list")

class QuiTitreDeleteView(DeleteView):
    model = QuiTitre
    template_name = "quititre_confirm_delete.html"
    success_url = reverse_lazy("quititre_list")
