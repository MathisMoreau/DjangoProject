from datetime import datetime
from django.db import models


class Machine(models.Model):
    TYPE = (
        ('PC', ('PC - Run windows')) ,
        ('Mac', ('MAc - Run MacOS')) ,
        ('Serveur', ('Serveur - Simple Server to deploy virtual machines ')),
        ('Switch', ('Switch To maintains and connect servers')),
        ('Router', ('Router To connect internet')),
    )
    infrastructure= models.CharField(max_length=20,default="..")
    id = models.AutoField( primary_key =True , editable = False )
    nom = models.CharField( max_length =6 )
    maintenanceDate = models.DateField(default = datetime.now())
    mach = models.CharField(max_length =32, choices=TYPE, default ='PC')

    def __str__(self):
        return str(self.id) + " -> " + self.nom

    def get_name(self):
        return str(self.id) + " " + self.nom

class Moi(models.Model):
    id=models.AutoField(
                primary_key=True,
                editable=False)
    username=models.CharField(max_length=40,default="..")
    password=models.CharField(max_length=30,default="..")
    nom=models.CharField(max_length=6)
    prenom=models.CharField(max_length=15)
    poste=models.TextField(max_length=40,default="..")
    adresse_mail=models.CharField(max_length=40,default="..")
    def __str__(self):
        return str(self.id) + " -> " + self.nom
    def get_name(self):
        return str(self.id) + " " + self.nom

class Infra(models.Model):
    id=models.AutoField(primary_key=True , editable= False)
    nom=models.TextField(max_length=20)
    nb_machines=models.IntegerField(default=0)
    Responsable=models.TextField(max_length=20)
    entretien=models.DateField(default=datetime.now())
    def __str__(self):
        return str(self.id) + " -> " + self.nom
    def get_name(self):
        return str(self.id) + " " + self.nom