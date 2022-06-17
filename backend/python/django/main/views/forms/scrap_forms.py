from django import forms

class MultiForm(forms.Form):
    CHOICES =(
    ("1", "Naveen"),
    ("2", "Pranav"),
    ("3", "Isha"),
    ("4", "Saloni"),
)
    geeks_field = forms.MultipleChoiceField(choices = CHOICES)

class ScrapForm(forms.Form):

    check_list = forms.MultiValueField(fields=[])
    pass