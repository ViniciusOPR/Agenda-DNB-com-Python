
from django import forms
from django.core.exceptions import ValidationError

from . import models


class ContactForm(forms.ModelForm):
    artistic_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'classe-a classe-b', 'placeholder': 'Digite seu AKA', }),
                          label='Artistic Name', help_text='Help text for users')
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs.update({
        #     'class': 'classe-a classe-b',
        #     'placeholder': 'Aqui veio do init',
        # })

    class Meta:
        model = models.Contact
        fields = ('artistic_name', 'name', 'phone', 'email', 'description', 'category')

        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'classe-a classe-b',
        #             'placeholder': 'Escreva aqui',
        #         }
        #     )
        # }

    def clean(self):
        cleaned_data = self.cleaned_data
        artistic_name = cleaned_data.get('artistic_name')
        name = cleaned_data.get('name')
        '''
        if aka == name:
            msg = ValidationError(
                'Primeiro nome não pode ser igual ao segundo',
                code='invalid'
            )
        
        self.add_error('AKA', msg)
        self.add_error('name', msg)
       '''
       
        return super().clean()
    def clean_first_name(self):
        artistic_name = self.cleaned_data.get('artistic_name')

       