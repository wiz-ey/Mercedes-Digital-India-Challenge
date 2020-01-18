from django.db import models

# Create your models here.
class New(models.Model):
    contract_status_choices = (
        ('1,0,0,0', 'Option-1'),
        ('0,1,0,0', 'Option-2'),
        ('0,0,1,0', 'Option-3'),
        ('0,0,0,1', 'Option-4'),

    )
    term_choices = (
        ('1,0', 'Short-Term'),
        ('0,1', 'Long-Term')
    )
    credit_score = models.FloatField()
    outstanding_amt = models.FloatField()
    maturity_day = models.FloatField()
    monthly_installment = models.FloatField()
    contract_status = models.CharField(max_length=10, choices=contract_status_choices)
    term_status = models.CharField(max_length=10, choices=term_choices)
