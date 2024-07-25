from django.db import models

# Create your models here.
class Approval(models.Model):
    """Approval model
    """
    GENDER_CHOICES  = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    MARRIED_CHOICES = (
        ('No', 'No'),
        ('Yes', 'Yes')
    )
    EDUCATION_CHOICES = (
        ('Graduate', 'Graduate'),
        ('Not Graduate', 'Not Graduate')
    )
    SELF_EMPLOYED_CHOICES = (
        ('No', 'No'),
        ('Yes', 'Yes')
    )
    PROPERTY_AREA_CHOICES = (
        ('Semiurban', 'Semiurban'),
        ('Urban', 'Urban'),
        ('Rural', 'Rural')
    )

    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    married = models.CharField(max_length=15, choices=MARRIED_CHOICES)
    dependents = models.IntegerField(default=0)
    education = models.CharField(max_length=15, choices=EDUCATION_CHOICES)
    self_employed = models.CharField(max_length=15, choices=SELF_EMPLOYED_CHOICES)
    application_income = models.IntegerField(default=0)
    coapplication_income = models.IntegerField(default=0)
    loan_amount = models.FloatField(default=0)
    loan_amount_term = models.FloatField(default=0)
    credit_history = models.IntegerField(default=0)
    property_area = models.CharField(max_length=15, choices=PROPERTY_AREA_CHOICES)

    def __str__(self):
        return self.first_name
