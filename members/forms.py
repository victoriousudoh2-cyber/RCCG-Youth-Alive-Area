
from django import forms
from .models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member

        fields = [
            "surname",
            "first_name",
            "last_name",
            "gender",
            "phone_number",
            "email",
            "date_of_birth",
            "home_address",
            "nationality",
            "state_of_origin",
            "home_town",
            "educational_qualification",
            "occupation",
            "occupation_address",
            "marital_status",
            "born_again",
            "baptized_by_immersion",
            "is_worker",
            "is_minister",
            "is_member",
            "departments",
        ]

        labels = {
            "last_name": "Middle Name",
            "phone_number": "Phone Number",
            "date_of_birth": "Date of Birth",
            "home_address": "Home Address",
            "home_town": "Home Town",
            "occupation_address": "Occupation Address",
            "born_again": "Are you born again?",
            "baptized_by_immersion": "Have you been baptized in water by immersion?",
            "is_worker": "Worker",
            "is_minister": "Minister",
            "is_member": "Member",
            "departments": "Department(s)",
        }

        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
            "marital_status": forms.RadioSelect(),
            "born_again": forms.RadioSelect(),
            "baptized_by_immersion": forms.RadioSelect(),
            "home_address": forms.Textarea(attrs={"rows": 2}),
            "occupation_address": forms.Textarea(attrs={"rows": 2}),
            "departments": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Write your department(s) here..."
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if isinstance(field.widget, forms.RadioSelect):
                field.widget.attrs["class"] = "form-check-input"

            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs["class"] = "form-check-input"

            elif isinstance(field.widget, forms.Select):
                field.widget.attrs["class"] = "form-select"

            else:
                field.widget.attrs["class"] = "form-control"
