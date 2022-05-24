from TD1App.models import Machine

class createMachineForm(forms.Form):
    nom=forms.Charfield(
        label="Nom de la machine"
    )
    def clean_nom(self):
        data=self.cleaned_data["nom"]
        if len(data) != 6:
            raise ValidationError(_("Erreur de format pour le champ 'nom"))
        return data