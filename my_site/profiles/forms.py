from django import forms


class FileUploadForm(forms.Form):
    image = forms.FileField()
