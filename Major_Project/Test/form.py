from django import forms

class DiseaseFinderForm(forms.Form):
    SYMPTOM_CHOICES = (
        ('Symptom_1', 'Vomiting'),
        ('Symptom_2', 'Cough'),
        ('Symptom_3', 'Acidity'),
        # Add more symptom choices here
    )
    symptoms = forms.MultipleChoiceField(
        choices=SYMPTOM_CHOICES,
        widget=forms.CheckboxSelectMultiple,
    )
