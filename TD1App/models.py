from datetime import datetime
from django.db import models


class Machine(models.Model):
    TYPE = (
        ('PC', ('PC - Run windows')) ,
        ('Mac', ('MAc - Run MacOS')) ,
        ('Serveur', ('Serveur - Simple Server to deploy virtual machines ')),
        ('Switch', ('Switch To maintains and connect servers')),
    )
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
    nom=models.CharField(
                max_length=6)
    def __str__(self):
        return str(self.id) + "MOI" + self.nom
    def get_name(self):
        return str(self.id) + " " + self.nom
