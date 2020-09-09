import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE' , 'jobs_project.settings')
import django
django.setup()
from random import randint
from faker import Faker
from testapp.models import *


fake = Faker()

def phoneNumberGen():
    d1 = randint(7 , 9)
    num = ""+str(d1)
    for i in range(0,9):
        num += str(randint(0 , 9))
    return int(num)

def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements = ('Project Manager' ,'Teamlead','Software'))
        feligibility = fake.random_element(elements=('B.Tech' ,'M.Tech','MCA','Phd'))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phoneNumberGen()
        hyd_jobs_record = punejobs.objects.get_or_create(date = fdate, company = fcompany, title = ftitle, eligibility = feligibility,address = faddress, email = femail, phonenumber = fphonenumber)

populate(100)
