from django.test import TestCase
from core.erp.models import *

print(Category.objects.all())

for i in Category.objects.filter():
  print(i)
