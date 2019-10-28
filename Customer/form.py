from django import forms

class CustomerForm(forms.Form):
    password= forms.CharField(widget=forms.PasswordInput())
    firstName = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'firstname'}))
    middleName = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Middlename','default':''}),required=False)
    lastName = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Lastname'}))
    mobileNo =  forms.RegexField(regex=r'^\+?1?\d{9,15}$')
    userName = forms.CharField()
    emailAdd = forms.EmailField(widget=forms.EmailInput(attrs={'id':'emlfld','name':'custeml'}))
    age = forms.IntegerField()
    temporaryAddress = forms.CharField(widget=forms.Textarea(attrs={'height':'70px'}))
    permanentAddress = forms.CharField(widget=forms.Textarea(attrs={'height':'70px'}))
    tPincode = forms.IntegerField()
    pPincode = forms.IntegerField()
    # gender = forms.CharField()
    # empId = forms.IntegerField()