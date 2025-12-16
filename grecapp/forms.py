from django import forms

class LoginForm(forms.Form):
    login = forms.CharField(label="Login", max_length=150)
    mdp = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


    # app/forms.py
from django import forms
from .models import (
    TypeAgent, TopoDom, Entite, Agent, Cadastre, Indice,
    Personne, TypeOperation, Operation, AvisPayement, Quittance,
    QuiCadastre, OpQuittance, QuittancePersonne, Titre, QuiTitre
)

class TypeAgentForm(forms.ModelForm):
    class Meta:
        model = TypeAgent
        fields = '__all__'

class TopoDomForm(forms.ModelForm):
    class Meta:
        model = TopoDom
        fields = '__all__'

class EntiteForm(forms.ModelForm):
    class Meta:
        model = Entite
        fields = '__all__'

class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = '__all__'

class CadastreForm(forms.ModelForm):
    class Meta:
        model = Cadastre
        fields = '__all__'

class IndiceForm(forms.ModelForm):
    class Meta:
        model = Indice
        fields = '__all__'

class PersonneForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = '__all__'

class TypeOperationForm(forms.ModelForm):
    class Meta:
        model = TypeOperation
        fields = '__all__'

class OperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = '__all__'

class AvisPayementForm(forms.ModelForm):
    class Meta:
        model = AvisPayement
        fields = '__all__'

class QuittanceForm(forms.ModelForm):
    class Meta:
        model = Quittance
        fields = '__all__'

class QuiCadastreForm(forms.ModelForm):
    class Meta:
        model = QuiCadastre
        fields = '__all__'

class OpQuittanceForm(forms.ModelForm):
    class Meta:
        model = OpQuittance
        fields = '__all__'

class QuittancePersonneForm(forms.ModelForm):
    class Meta:
        model = QuittancePersonne
        fields = '__all__'

class TitreForm(forms.ModelForm):
    class Meta:
        model = Titre
        fields = '__all__'

class QuiTitreForm(forms.ModelForm):
    class Meta:
        model = QuiTitre
        fields = '__all__'
