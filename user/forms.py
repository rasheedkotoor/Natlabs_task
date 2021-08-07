from django import forms
from django.contrib.auth.forms import UserCreationForm as UForm
from .models import User


class UserSignUpForm(UForm):
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'input'}))

    class Meta(UForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # @transaction.atomic
    # def save(self):
    #     user = super().save(commit=False)
    #     user.phone_number = self.cleaned_data.get('phone_number')
    #     user.save()
    #     student = Student.objects.create(user=user)
    #     student.save()
    #     return user
