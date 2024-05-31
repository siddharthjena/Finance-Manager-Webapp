from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    total_inc = models.IntegerField(null=True, blank=True, default=0)
    total_exp = models.IntegerField(null=True, blank=True, default=0)
    remaining = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.username

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_income = models.BooleanField(default=False)  # True for income, False for expense
    date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount} on {self.date}"


