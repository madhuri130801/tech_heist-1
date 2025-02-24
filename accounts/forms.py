from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    extra_field=forms.CharField(required=True)
    class Meta:
        fields = ("username", "email", "password1", "password2","extra_field")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"
        self.fields["extra_field"].label = "Interested Topics"

        
