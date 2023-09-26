from django import forms
from .models import Menu

class MenuForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title'
            }
        ),
    )

    class Meta:
        model = Menu
        fields = '__all__'