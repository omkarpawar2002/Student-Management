from django import forms
from .models import Student

gender_choices = [
    ('MALE','MALE'),
    ('FEMALE','FEMALE'),
    ('OTHER','OTHER')
]

subject_choices = [
    ('PHYSICS','PHYSICS'),
    ('CHEMISTRY','CHEMISTRY'),
    ('BIOLOGY','BIOLOGY'),
    ('ZOOLOGY','ZOOLOGY'),
    ('BOTANY','BOTANY'),
    ('IT','IT'),
    ('CS','CS'),
    ('AWS','AWS')
]

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'stu_id':'STUDENT ID',
            'first_name':'FIRST NAME',
            'last_name':'LAST NAME',
            'mobile':'MOBILE NO',
            'gender':'GENDER',
            'dob':'DATE OF BIRTH',
            'subject':'SUBJECT',
            'marks':'MARKS',
            'city':'CITY',
            'address':'ADDRESS',
            'email':'EMAIL ID',
            'password':'PASSWORD',
            'eligble':'ELIGIBILITY'
        }
        widgets = {
            'stu_id':forms.NumberInput(attrs={
                'placeholder':'E.g.,101',
            }),
            'first_name':forms.TextInput(attrs={
                'placeholder':'Enter First Name',
            }),
            'last_name':forms.TextInput(attrs={
                'placeholder':'Enter Last Name',
            }),
            'mobile':forms.TextInput(attrs={
                'placeholder':'E.g., +91 **********',
            }),
            'gender':forms.RadioSelect(choices=gender_choices),
            'dob':forms.DateInput(attrs={
                'type':'date',
            }),
            'subject':forms.Select(choices=subject_choices),
            'city':forms.TextInput(attrs={
                'placeholder':'E.g.,Mumbai',
            }),
            'address':forms.Textarea(attrs={
                'placeholder':'E.g.,Mumbai , Maharashtra',
                'rows':'2',
            }),
            'email':forms.EmailInput(attrs={
                'placeholder':'youremail@gmail.com',
            }),
            'password':forms.PasswordInput(attrs={
                'type':'password',
            })
        }