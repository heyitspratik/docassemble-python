from django.db import models
from djmoney.models.fields import MoneyField


currency_choices= (
        ('USD','USD'),
        ('GBP','GBP'),
        ('EUR','EUR')
    )

class QuestionData(models.Model):
    question = models.CharField(max_length=100,blank=True,null=True)
    currency = models.CharField(max_length=25, choices=currency_choices,default="USD")
    value = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = 'Question data'
        verbose_name_plural = 'Question data'