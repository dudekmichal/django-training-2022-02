from django.db import models


class Guard(models.Model):
    RANK_CHOICES = {
        ('T', 'Triangle'),
        ('S', 'Square'),
        ('C', 'Circle')
    }
    name = models.CharField(max_length=50)
    rank = models.CharField(
        max_length=1,
        choices=RANK_CHOICES,
        default='C'
    )
    salary = models.PositiveIntegerField(default=1000)


class Person(models.Model):
    GENDER_CHOICES = {
        ('U', 'Unknown'),
        ('M', 'Male'),
        ('F', 'Female'),
        ('NB', 'Nonbinary')
    }
    STATE_CHOICES = {
        ('D', 'Dead'),
        ('A', 'Alive')
    }
    age = models.IntegerField(blank=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12, blank=True)
    email = models.EmailField(blank=True)
    debt = models.PositiveIntegerField(blank=True)
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        default=('U', 'Unknown')
    )
    profession = models.CharField(max_length=100,
                                  blank=True)
    weight = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    number = models.PositiveIntegerField(blank=True, null=True)
    state = models.CharField(
        max_length=1,
        choices=STATE_CHOICES,
        default='A'
    )
    recruitment_date = models.DateField(auto_now_add=True, null=True)


class Suit(models.Model):
    SIZE_CHOICES = models.TextChoices('Size', 'S M L')

    GENDER_CHOICES = {
        ('M', 'Male'),
        ('F', 'Female'),
    }
    COLOUR_CHOICES = {
        ('R', 'Red'),
        ('G', 'Green')
    }
    size = models.CharField(
        max_length=1,
        choices=SIZE_CHOICES.choices,
        default='M'
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default='M'
    )
    colour = models.CharField(
        max_length=1,
        choices=COLOUR_CHOICES,
        default='R'
    )
