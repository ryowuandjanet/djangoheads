from django.test import TestCase
from core.erp.models import *

obj=Employee.objects.filter()

for i in Type.objects.filter():
  print(i.name)
