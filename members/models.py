
from django.db import models


class Member(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]

    MARITAL_STATUS_CHOICES = [
        ("Single", "Single"),
        ("Married", "Married"),
        ("Engaged", "Engaged"),
        ("Divorced", "Divorced"),
        ("Widowed", "Widowed"),
    ]

    YES_NO_CHOICES = [
        ("Yes", "Yes"),
        ("No", "No"),
    ]

    surname = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    home_address = models.TextField(blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    state_of_origin = models.CharField(max_length=100, blank=True)
    home_town = models.CharField(max_length=150, blank=True)
    educational_qualification = models.CharField(max_length=200, blank=True)
    occupation = models.CharField(max_length=200, blank=True)
    occupation_address = models.TextField(blank=True)
    marital_status = models.CharField(
        max_length=20, choices=MARITAL_STATUS_CHOICES, blank=True
    )
    born_again = models.CharField(max_length=5, choices=YES_NO_CHOICES, blank=True)
    baptized_by_immersion = models.CharField(
        max_length=5, choices=YES_NO_CHOICES, blank=True
    )
    is_worker = models.BooleanField(default=False)
    is_minister = models.BooleanField(default=False)
    is_member = models.BooleanField(default=False)
    departments = models.TextField(blank=True)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.surname} {self.first_name} {self.last_name}"
