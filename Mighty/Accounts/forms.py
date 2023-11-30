from django import forms
from .models import UserAdmin
from django.contrib.auth.forms import UserCreationForm


class DateInput(forms.DateInput):
    input_type = 'date'

class AdminForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'style': 'max-width: 20em'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'style': 'max-width: 20em'})
    class Meta:
        model = UserAdmin
        fields =('fname','lname','username','email','birthdate','gender','password1','password2')

        widgets={
                'fname':forms.TextInput(attrs={'class':'form-control ','style':'max-width: 20em',"id":"","placeholder":""}),
                'lname':forms.TextInput(attrs={'class':'form-control','style':'max-width: 20em',"id":"","placeholder":""}),
                'email':forms.TextInput(attrs={'class':'form-control ','style':'max-width: 20em',"id":"","placeholder":""}),
                'username':forms.TextInput(attrs={'class':'form-control ','style':'max-width: 20em',"placeholder":""}),
                'birthdate':DateInput(attrs={'class':'form-control ','style':' max-width: 20em',"id":"","placeholder":"29/09/1996"}),
                'gender': forms.Select(attrs={'class':'form-control ','style':'max-width: 20em',"id":"","placeholder":""}),
                #'is_subscriped': forms.CheckboxInput(attrs={'class':'form-check-input ','style':' margin-left:20px',"id":"","placeholder":""}),
          }  
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['class'] = 'form-control'   
        
     
   





class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','name':'password'}))





