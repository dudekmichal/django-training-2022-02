import re
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(message="Number must be even!")


def validate_positive(value):
    if value <= 0:
        raise ValidationError(message="Number must be positive!")


def validate_3_digits_number(number):
    if number >= 1000:
        raise ValidationError(message="Number should contain max 3 digits.")


def validate_minimal_weight(weight):
    if weight <= 30:
        raise ValidationError(message="Weight must be above 30kg.")


def validate_minimal_debt(debt):
    if debt <= 10000:
        raise ValidationError(message="Debt must be above 10000.")


def validate_phone_number_format(phone_number):
    pattern = re.compile("^\d{3}-\d{3}-\d{3}$")
    if not pattern.match(phone_number):
        raise ValidationError(message="Phone number should be in XXX-XXX-XXX format.")


class Person(models.Model):

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Age {self.age}"

    @staticmethod
    def get_all_competitors():
        return Person.objects.all()

    @staticmethod
    def get_all_competitors_count():
        all_competitors = Person.get_all_competitors()
        return all_competitors.count()

    @staticmethod
    def get_alive_competitors_count():
        all_competitors = Person.get_all_competitors()
        return all_competitors.filter(state="A").count()

    @staticmethod
    def get_alive_competitors():
        all_competitors = Person.get_all_competitors()
        return all_competitors.filter(state="A")

    @staticmethod
    def get_debt_summary():
        all_competitors = Person.get_all_competitors()
        return sum([competitor.debt for competitor in all_competitors if isinstance(competitor.debt, int)])

    @staticmethod
    def get_current_prize():
        TOTAL_PRIZE = 45600000
        alive_competitors_count = Person.get_alive_competitors_count()
        current_prize = 0 if not alive_competitors_count else TOTAL_PRIZE / alive_competitors_count
        return current_prize

    @staticmethod
    def get_player_by_id(id):
        return Person.objects.get(pk=id)

    SEX_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
        ('U', 'Unknown',)
    )

    STATE_CHOICES = {
        ('D', 'Dead'),
        ('A', 'Alive')
    }

    age = models.PositiveSmallIntegerField(validators=[validate_positive, validate_even])
    name = models.CharField(max_length=20, default="Unknown")
    phone = PhoneNumberField(blank=True)
    email = models.EmailField(blank=True)
    debt = models.PositiveBigIntegerField(default=0, validators=[validate_minimal_debt])
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default=('U', 'Unknown',))
    profession = models.CharField(blank=True, max_length=20)
    weight = models.PositiveIntegerField(blank=True, null=True, validators=[validate_minimal_weight])
    height = models.PositiveIntegerField(blank=True, null=True)
    state = models.CharField(max_length=1, choices=STATE_CHOICES, default='A')
    recruitment_date = models.DateField(auto_now_add=True)
    number = models.PositiveIntegerField(blank=True, null=True, validators=[validate_3_digits_number])


class Guard(models.Model):

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Rank: {self.rank}"

    RANK_CHOICES = {
        ('T', 'Triangle'),
        ('S', 'Square'),
        ('C', 'Circle')
    }

    name = models.CharField(max_length=50)
    rank = models.CharField(max_length=1, choices=RANK_CHOICES, default='C')
    salary = models.PositiveIntegerField(default=1000)


class Suit(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"ID: {self.id}, Size: {self.size}, Gender {self.gender}, Colour: {self.colour}"

    SIZE_CHOICES = models.TextChoices('Size', 'S M L')

    GENDER_CHOICES = {
        ('M', 'Male'),
        ('F', 'Female'),
    }
    COLOUR_CHOICES = {
        ('R', 'Red'),
        ('G', 'Green')
    }

    size = models.CharField(max_length=1, choices=SIZE_CHOICES.choices, default='M')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    colour = models.CharField(max_length=1, choices=COLOUR_CHOICES, default='R')
