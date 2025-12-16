from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("encaissement/", views.encaissement, name="encaissement"),
]


# app/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    # ------------------------------
    # TYPEAGENT
    # ------------------------------
    path("typeagents/", TypeAgentListView.as_view(), name="typeagent_list"),
    path("typeagents/<int:pk>/", TypeAgentDetailView.as_view(), name="typeagent_detail"),
    path("typeagents/create/", TypeAgentCreateView.as_view(), name="typeagent_create"),
    path("typeagents/<int:pk>/update/", TypeAgentUpdateView.as_view(), name="typeagent_update"),
    path("typeagents/<int:pk>/delete/", TypeAgentDeleteView.as_view(), name="typeagent_delete"),

    # ------------------------------
    # TOPODOM
    # ------------------------------
    path("topodoms/", TopoDomListView.as_view(), name="topodom_list"),
    path("topodoms/<int:pk>/", TopoDomDetailView.as_view(), name="topodom_detail"),
    path("topodoms/create/", TopoDomCreateView.as_view(), name="topodom_create"),
    path("topodoms/<int:pk>/update/", TopoDomUpdateView.as_view(), name="topodom_update"),
    path("topodoms/<int:pk>/delete/", TopoDomDeleteView.as_view(), name="topodom_delete"),

    # ------------------------------
    # ENTITE
    # ------------------------------
    path("entites/", EntiteListView.as_view(), name="entite_list"),
    path("entites/<int:pk>/", EntiteDetailView.as_view(), name="entite_detail"),
    path("entites/create/", EntiteCreateView.as_view(), name="entite_create"),
    path("entites/<int:pk>/update/", EntiteUpdateView.as_view(), name="entite_update"),
    path("entites/<int:pk>/delete/", EntiteDeleteView.as_view(), name="entite_delete"),

    # ------------------------------
    # AGENT
    # ------------------------------
    path("agents/", AgentListView.as_view(), name="agent_list"),
    path("agents/<int:pk>/", AgentDetailView.as_view(), name="agent_detail"),
    path("agents/create/", AgentCreateView.as_view(), name="agent_create"),
    path("agents/<int:pk>/update/", AgentUpdateView.as_view(), name="agent_update"),
    path("agents/<int:pk>/delete/", AgentDeleteView.as_view(), name="agent_delete"),

    # ------------------------------
    # CADASTRE
    # ------------------------------
    path("cadastres/", CadastreListView.as_view(), name="cadastre_list"),
    path("cadastres/<int:pk>/", CadastreDetailView.as_view(), name="cadastre_detail"),
    path("cadastres/create/", CadastreCreateView.as_view(), name="cadastre_create"),
    path("cadastres/<int:pk>/update/", CadastreUpdateView.as_view(), name="cadastre_update"),
    path("cadastres/<int:pk>/delete/", CadastreDeleteView.as_view(), name="cadastre_delete"),

    # ------------------------------
    # INDICE
    # ------------------------------
    path("indices/", IndiceListView.as_view(), name="indice_list"),
    path("indices/<int:pk>/", IndiceDetailView.as_view(), name="indice_detail"),
    path("indices/create/", IndiceCreateView.as_view(), name="indice_create"),
    path("indices/<int:pk>/update/", IndiceUpdateView.as_view(), name="indice_update"),
    path("indices/<int:pk>/delete/", IndiceDeleteView.as_view(), name="indice_delete"),

    # ------------------------------
    # PERSONNE
    # ------------------------------
    path("personnes/", PersonneListView.as_view(), name="personne_list"),
    path("personnes/<int:pk>/", PersonneDetailView.as_view(), name="personne_detail"),
    path("personnes/create/", PersonneCreateView.as_view(), name="personne_create"),
    path("personnes/<int:pk>/update/", PersonneUpdateView.as_view(), name="personne_update"),
    path("personnes/<int:pk>/delete/", PersonneDeleteView.as_view(), name="personne_delete"),

    # ------------------------------
    # TYPEOPERATION
    # ------------------------------
    path("typeoperations/", TypeOperationListView.as_view(), name="typeoperation_list"),
    path("typeoperations/<int:pk>/", TypeOperationDetailView.as_view(), name="typeoperation_detail"),
    path("typeoperations/create/", TypeOperationCreateView.as_view(), name="typeoperation_create"),
    path("typeoperations/<int:pk>/update/", TypeOperationUpdateView.as_view(), name="typeoperation_update"),
    path("typeoperations/<int:pk>/delete/", TypeOperationDeleteView.as_view(), name="typeoperation_delete"),

    # ------------------------------
    # OPERATION
    # ------------------------------
    path("operations/", OperationListView.as_view(), name="operation_list"),
    path("operations/<int:pk>/", OperationDetailView.as_view(), name="operation_detail"),
    path("operations/create/", OperationCreateView.as_view(), name="operation_create"),
    path("operations/<int:pk>/update/", OperationUpdateView.as_view(), name="operation_update"),
    path("operations/<int:pk>/delete/", OperationDeleteView.as_view(), name="operation_delete"),

    # ------------------------------
    # AVISPAYEMENT
    # ------------------------------
    path("avispayements/", AvisPayementListView.as_view(), name="avispayement_list"),
    path("avispayements/<int:pk>/", AvisPayementDetailView.as_view(), name="avispayement_detail"),
    path("avispayements/create/", AvisPayementCreateView.as_view(), name="avispayement_create"),
    path("avispayements/<int:pk>/update/", AvisPayementUpdateView.as_view(), name="avispayement_update"),
    path("avispayements/<int:pk>/delete/", AvisPayementDeleteView.as_view(), name="avispayement_delete"),

    # ------------------------------
    # QUITTANCE
    # ------------------------------
    path("quittances/", QuittanceListView.as_view(), name="quittance_list"),
    path("quittances/<int:pk>/", QuittanceDetailView.as_view(), name="quittance_detail"),
    path("quittances/create/", QuittanceCreateView.as_view(), name="quittance_create"),
    path("quittances/<int:pk>/update/", QuittanceUpdateView.as_view(), name="quittance_update"),
    path("quittances/<int:pk>/delete/", QuittanceDeleteView.as_view(), name="quittance_delete"),

    # ------------------------------
    # QUICADASTRE
    # ------------------------------
    path("quicadastres/", QuiCadastreListView.as_view(), name="quicadastre_list"),
    path("quicadastres/<int:pk>/", QuiCadastreDetailView.as_view(), name="quicadastre_detail"),
    path("quicadastres/create/", QuiCadastreCreateView.as_view(), name="quicadastre_create"),
    path("quicadastres/<int:pk>/update/", QuiCadastreUpdateView.as_view(), name="quicadastre_update"),
    path("quicadastres/<int:pk>/delete/", QuiCadastreDeleteView.as_view(), name="quicadastre_delete"),

    # ------------------------------
    # OPQUITTANCE
    # ------------------------------
    path("opquittances/", OpQuittanceListView.as_view(), name="opquittance_list"),
    path("opquittances/<int:pk>/", OpQuittanceDetailView.as_view(), name="opquittance_detail"),
    path("opquittances/create/", OpQuittanceCreateView.as_view(), name="opquittance_create"),
    path("opquittances/<int:pk>/update/", OpQuittanceUpdateView.as_view(), name="opquittance_update"),
    path("opquittances/<int:pk>/delete/", OpQuittanceDeleteView.as_view(), name="opquittance_delete"),

    # ------------------------------
    # QUITTANCEPERSONNE
    # ------------------------------
    path("quittancepersonnes/", QuittancePersonneListView.as_view(), name="quittancepersonne_list"),
    path("quittancepersonnes/<int:pk>/", QuittancePersonneDetailView.as_view(), name="quittancepersonne_detail"),
    path("quittancepersonnes/create/", QuittancePersonneCreateView.as_view(), name="quittancepersonne_create"),
    path("quittancepersonnes/<int:pk>/update/", QuittancePersonneUpdateView.as_view(), name="quittancepersonne_update"),
    path("quittancepersonnes/<int:pk>/delete/", QuittancePersonneDeleteView.as_view(), name="quittancepersonne_delete"),

  # ------------------------------
    # TITRE
    # ------------------------------
    path("titres/", TitreListView.as_view(), name="titre_list"),
    path("titres/<int:pk>/", TitreDetailView.as_view(), name="titre_detail"),
    path("titres/create/", TitreCreateView.as_view(), name="titre_create"),
    path("titres/<int:pk>/update/", TitreUpdateView.as_view(), name="titre_update"),
    path("titres/<int:pk>/delete/", TitreDeleteView.as_view(), name="titre_delete"),

    # ------------------------------
    # QUITITRE
    # ------------------------------
    path("quititres/", QuiTitreListView.as_view(), name="quititre_list"),
    path("quititres/<int:pk>/", QuiTitreDetailView.as_view(), name="quititre_detail"),
    path("quititres/create/", QuiTitreCreateView.as_view(), name="quititre_create"),
    path("quititres/<int:pk>/update/", QuiTitreUpdateView.as_view(), name="quititre_update"),
    path("quititres/<int:pk>/delete/", QuiTitreDeleteView.as_view(), name="quititre_delete"),
]