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

    First_Name = models.CharField(max_length=15)
    Last_Name = models.CharField(max_length=15)
    Gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    Married = models.CharField(max_length=15, choices=MARRIED_CHOICES)
    Dependents = models.IntegerField(default=0)
    Education = models.CharField(max_length=15, choices=EDUCATION_CHOICES)
    Self_Employed = models.CharField(max_length=15, choices=SELF_EMPLOYED_CHOICES)
    ApplicantIncome = models.IntegerField(default=0)
    CoapplicantIncome = models.IntegerField(default=0)
    LoanAmount = models.FloatField(default=0)
    Loan_Amount_Term = models.FloatField(default=0)
    Credit_History = models.IntegerField(default=0)
    Property_Area = models.CharField(max_length=15, choices=PROPERTY_AREA_CHOICES)
    
    def __str__(self):
        return self.first_name
