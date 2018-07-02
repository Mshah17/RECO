from django.db import models


class Post(models.Model):
    title= models.CharField(max_length=140)
    body= models.TextField()
    date= models.DateTimeField()

    def __str__(self):
        return self.title


class Auth(models.Model):
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.user


class Login(models.Model):
    user1 = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)

    def __str__(self):
        return self.user1


class Medicinereco(models.Model):
    medicine = models.CharField(max_length=50)
    symptoms = models.CharField(max_length=50)
    dose = models.CharField(max_length=200)

    def ___str__(self):
        return self.medicine

    class Meta:
        ordering = ['symptoms']