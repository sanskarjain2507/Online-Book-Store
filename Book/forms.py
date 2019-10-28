from django import forms

class BookForm(forms.Form):
    bookId = forms.IntegerField()
    title = forms.CharField()
    isbn = forms.CharField()
    language = forms.CharField()
    publisher = forms.CharField()
    author = forms.CharField()
    mrp = forms.IntegerField()
    publishYear = forms.CharField()
    quantity = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea())
    rating = forms.IntegerField()
    category=forms.CharField()
    image = forms.ImageField()