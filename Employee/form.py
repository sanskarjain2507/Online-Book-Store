from .models import Employee
from django import forms

class EmployeeForm(forms.ModelForm):

    # temporaryAddress= forms.Textarea(attrs={'height':'200px', 'width':'200px'})
    class Meta:
        model = Employee
        fields = ('firstName','middleName','lastName','mobileNo','empName','password','temporaryAddress','emailAdd','salary','experience','age','tPincode','permanentAddress','pPincode')

class EmployeeForm1(forms.Form):
    password= forms.CharField(widget=forms.PasswordInput())
    firstName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'firstname'}),error_messages={'invalid':'Enter a valid first name'})
    middleName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Middlename'}),required=False,error_messages={'invalid':'Enter a valid middle name'})
    lastName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Lastname'}),error_messages={'invalid':'Enter a valid  last name'})
    mobileNo =  forms.RegexField(regex=r'^\+?1?\d{9,15}$',error_messages={'invalid':'Enter a valid mobile number'})
    empName = forms.CharField(error_messages={'invalid':'Enter a valid employee name'})
    emailAdd = forms.EmailField(widget=forms.EmailInput(attrs={'id':'emlfld','name':'empeml'}),error_messages={'invalid':'Enter a valid email'})
    salary = forms.IntegerField(error_messages={'invalid':'Enter a valid salary'})
    experience = forms.IntegerField(error_messages={'invalid':'Enter your valid experience'})
    age = forms.IntegerField(error_messages={'invalid':'Enter your valid age'})
    temporaryAddress = forms.CharField(widget=forms.Textarea(),error_messages={'invalid':'Enter a valid address'})
    tPincode = forms.IntegerField(error_messages={'invalid':'Enter a valid pin code'})
    permanentAddress = forms.CharField(widget=forms.Textarea(),error_messages={'invalid':'Enter a valid address'})
    pPincode = forms.IntegerField(error_messages={'invalid':'Enter a valid pincode'})
    # gender = forms.CharField()
    # empId = forms.IntegerField()
    