from django import forms

class TaskCreateForm(forms.Form):
    task_name = forms.CharField(max_length=120)
    date = forms.CharField(max_length=50)
    status = forms.CharField(max_length=60)

    def clean(self):
        print('inside clean')

class TaskSearch(forms.Form):
    date = forms.CharField(max_length=50)

class TaskUpdateForm(forms.Form):
    id = forms.CharField(max_length=12)
    task_name = forms.CharField(max_length=120)
    date = forms.CharField(max_length=50)
    status = forms.CharField(max_length=60)

    def clean(self):
        print('inside clean')