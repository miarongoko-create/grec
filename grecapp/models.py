from django.db import models

# Create your models here.

# ------------------------------
#        TABLE DE BASE
# ------------------------------

class TypeAgent(models.Model):
    idtype = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=150)

    def __str__(self):
        return self.libelle


class TopoDom(models.Model):
    idtopdom = models.AutoField(primary_key=True)
    litopdom = models.CharField(max_length=150)
    direction = models.CharField(max_length=150)
    photo = models.CharField(max_length=255, blank=True, null=True,default=None)

    def __str__(self):
        return self.litopdom


class Entite(models.Model):
    identite = models.AutoField(primary_key=True)
    idtopdom = models.ForeignKey(TopoDom, on_delete=models.CASCADE)
    libentite = models.CharField(max_length=150)
    abrev = models.CharField(max_length=50)
    img = models.ImageField(upload_to="entites/")
    sigle = models.CharField(max_length=50)

    def __str__(self):
        return self.libentite


# ------------------------------
#        AGENT
# ------------------------------

class Agent(models.Model):
    idagent = models.AutoField(primary_key=True)
    identite = models.ForeignKey(Entite, on_delete=models.CASCADE)
    idtype = models.ForeignKey(TypeAgent, on_delete=models.CASCADE)
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    login = models.CharField(max_length=100, unique=True)
    mdp = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    sigleAg = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nom} {self.prenom}"


# ------------------------------
#        CADASTRE – INDICE
# ------------------------------

class Cadastre(models.Model):
    idcadastre = models.BigAutoField(primary_key=True)
    registre = models.CharField(max_length=150)
    folio = models.CharField(max_length=150)
    section = models.CharField(max_length=150)
    dite = models.CharField(max_length=255)
    commune = models.CharField(max_length=150)
    parcelle = models.CharField(max_length=150)
    libcadastre = models.CharField(max_length=255)

    def __str__(self):
        return self.libcadastre


class Indice(models.Model):
    idindice = models.AutoField(primary_key=True)
    identite = models.ForeignKey(Entite, on_delete=models.CASCADE)
    indice = models.CharField(max_length=150)
    commune = models.CharField(max_length=100)
    district = models.CharField(max_length=100)

    def __str__(self):
        return self.indice


# ------------------------------
#        PERSONNE
# ------------------------------

class Personne(models.Model):
    idpersonne = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    cin = models.CharField(max_length=50)
    datecin = models.CharField(max_length=50)
    lieucin = models.CharField(max_length=150)
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=50)
    statut = models.CharField(max_length=50)
    infostatut = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nom} {self.prenom}"


# ------------------------------
#        OPERATION
# ------------------------------

class TypeOperation(models.Model):
    idtypeoperation = models.AutoField(primary_key=True)
    type = models.CharField(max_length=150)

    def __str__(self):
        return self.type


class Operation(models.Model):
    idoperation = models.AutoField(primary_key=True)
    idtopdom = models.ForeignKey(TopoDom, on_delete=models.CASCADE)
    idtypeoperation = models.ForeignKey(TypeOperation, on_delete=models.CASCADE)
    liboperation = models.CharField(max_length=150)
    cout = models.CharField(max_length=100)
    sigle = models.CharField(max_length=50)

    def __str__(self):
        return self.liboperation


# ------------------------------
#        AVIS PAYEMENT
# ------------------------------

class AvisPayement(models.Model):
    idavispayement = models.AutoField(primary_key=True)
    montant = models.CharField(max_length=100)
    date = models.CharField(max_length=50)
    avance = models.CharField(max_length=100)
    dateavance = models.CharField(max_length=50)

    def __str__(self):
        return f"Avis {self.idavispayement}"


# ------------------------------
#        QUITTANCE
# ------------------------------

class Quittance(models.Model):
    idquittance = models.AutoField(primary_key=True)
    idavispayement = models.ForeignKey(AvisPayement, on_delete=models.CASCADE)
    idagent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    identite = models.ForeignKey(Entite, on_delete=models.CASCADE)
    refquittance = models.CharField(max_length=150)
    montant = models.CharField(max_length=100)
    date = models.CharField(max_length=50)
    topdom = models.CharField(max_length=150)
    avance = models.CharField(max_length=100)
    reste = models.CharField(max_length=100)
    refdossier = models.CharField(max_length=150)
    bureau = models.CharField(max_length=150)
    requisition = models.CharField(max_length=150)

    def __str__(self):
        return self.refquittance


# ------------------------------
#        TABLES D’ASSOCIATION
# ------------------------------

class QuiCadastre(models.Model):
    idcadastre = models.ForeignKey(Cadastre, on_delete=models.CASCADE)
    idquittance = models.ForeignKey(Quittance, on_delete=models.CASCADE)


class OpQuittance(models.Model):
    idquittance = models.ForeignKey(Quittance, on_delete=models.CASCADE)
    idoperation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    cout = models.CharField(max_length=100)
    nb = models.CharField(max_length=50)
    pu = models.CharField(max_length=50)


class QuittancePersonne(models.Model):
    idquittance = models.ForeignKey(Quittance, on_delete=models.CASCADE)
    idpersonne = models.ForeignKey(Personne, on_delete=models.CASCADE)
    typepersonne = models.CharField(max_length=50)


class Titre(models.Model):
    idtitre = models.AutoField(primary_key=True)
    libtitre = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.libtitre


class QuiTitre(models.Model):
    idtitre = models.ForeignKey(Titre, on_delete=models.CASCADE)
    idquittance = models.ForeignKey(Quittance, on_delete=models.CASCADE)

