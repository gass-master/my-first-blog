from django.db import models
from django.utils import timezone

"""Blog Tutorial"""

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


"""Global: Models for global data"""

class Currency(models.Model):
    isocode = models.CharField(max_length=3, unique=True)
    datevalend = models.DateTimeField()
    
class Nation(models.Model):
    isocode = models.CharField(max_length=2, unique=True)
    isocode2 = models.CharField(max_length=3, blank=True, null=True)
    carplate = models.CharField(max_length=3, blank=True, null=True)
    ziplenght = models.SmallIntegerField(blank=True, null=True)
    zipcheckrule = models.CharField(max_length=5, blank=True, null=True)
    zipmandatory = models.BooleanField()

class State(models.Model):
    state = models.CharField(max_length=2, unique=True)
    nation = models.ForeignKey('Nation', on_delete=models.CASCADE, to_field='isocode')

class Legalform(models.Model):
    PERSONAL = 'PS'
    CORPORATE = 'CR'
    LEGALTYPE_CHOICES = ((PERSONAL, 'Personal'), (CORPORATE, 'Corporate'),)
    legalform = models.CharField(max_length=2, unique=True)
    nation = models.ForeignKey('Nation', on_delete=models.CASCADE, to_field='isocode')
    legaltype = models.CharField(max_length=1, choices=LEGALTYPE_CHOICES)


"""Customer: Models for accounting customers"""

class Address(models.Model):
    DOMICILE = 'DO'
    POSTAL = 'PO'
    ADRTYPE_CHOICES = ((DOMICILE, 'Domicile'), (POSTAL, 'Postal'),)    
    adrid = models.CharField(max_length=10, unique=True)
    adrtype = models.CharField(max_length=2, choices=ADRTYPE_CHOICES)
    line1 = models.CharField(max_length=30, blank=True, null=True)
    line2 = models.CharField(max_length=30, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    state = models.ForeignKey('State', on_delete=models.CASCADE, to_field='state')
    country = models.ForeignKey('Nation', on_delete=models.CASCADE, to_field='isocode')

class Contact(models.Model):
    MR = 'MR'
    MRS = 'MRS'
    SALUT_CHOICES = ((MR, 'Mr.'), (MRS, 'Mrs.'),)
    CUST = 'CUST'
    ACC = 'ACC'
    CONTTYPE_CHOICES = ((CUST, 'Cstomer'), (ACC, 'Accountant'),)
    contid = models.CharField(max_length=10, unique=True)
    contgroup = models.CharField(max_length=5)
    conttype = models.CharField(max_length=5, choices=CONTTYPE_CHOICES)
    salut = models.CharField(max_length=3, choices=SALUT_CHOICES)
    first = models.CharField(max_length=30, blank=True, null=True)
    middle = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    position = models.CharField(max_length=30, blank=True, null=True)
    image = models.CharField(max_length=1, blank=True, null=True)
    role = models.CharField(max_length=1, blank=True, null=True)
    adrid = models.ForeignKey('Address', on_delete=models.CASCADE, to_field='adrid')
    
class Customer(models.Model):
    customerid = models.CharField(max_length=10, unique=True)
    customergroup = models.ForeignKey('Customergroup', on_delete=models.CASCADE, to_field='customergroup')
    legalform = models.ForeignKey('Legalform', on_delete=models.CASCADE, to_field='legalform')
    name1 = models.CharField(max_length=50)
    adrid = models.ForeignKey('Address', on_delete=models.CASCADE, to_field='adrid')
    compid = models.CharField(max_length=30, blank=True, null=True)
    vatid = models.CharField(max_length=30, blank=True, null=True)
    client = models.CharField(max_length=5, blank=True, null=True)
    logo = models.CharField(max_length=1, blank=True, null=True)
    www = models.CharField(max_length=50, blank=True, null=True)
    startup = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=5)
    accountant = models.CharField(max_length=10, blank=True, null=True)

class Customergroup(models.Model):
    customergroup = models.CharField(max_length=5, unique=True)
    description = models.CharField(max_length=30)
    norange = models.CharField(max_length=5, blank=True, null=True)

    

    
