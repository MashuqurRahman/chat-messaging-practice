from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=150, widget=forms.TextInput(attrs={'class':'fadeIn second','id':'login','placeholder' : "Username" }))

    password = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={'class':'fadeIn second form-control ','id':'password','placeholder' : "password"}))

  
    