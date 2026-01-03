from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Imię", max_length=100)
    email = forms.EmailField(label="Email")
    message = forms.CharField(
        label="Wiadomość",
        widget=forms.Textarea
    )
