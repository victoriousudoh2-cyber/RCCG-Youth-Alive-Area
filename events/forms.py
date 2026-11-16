
from django import forms
from .models import EventRegistration


class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = EventRegistration

        fields = [
            "event",
            "full_name",
            "email",
            "phone",
            "gender",
            "is_worker",
            "is_minister",
            "is_member",
        ]

        labels = {
            "full_name": "Full Name",
            "phone": "Phone Number",
            "gender": "Gender",
            "is_worker": "Worker",
            "is_minister": "Minister",
            "is_member": "Member",
        }

        widgets = {
            "gender": forms.Select(
                attrs={"class": "form-select"}
            ),
            "is_worker": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),
            "is_minister": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),
            "is_member": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name not in [
                "gender",
                "is_worker",
                "is_minister",
                "is_member",
            ]:
                field.widget.attrs["class"] = "form-control"
