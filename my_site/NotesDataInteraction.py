from office.models import Patient

# Create and insert data to Database

# .save() method
carl = Patient(first_name='Carl', last_name='Smith', age=30)
carl.save()
#.objects.create()
Patient.objects.create(first_name='Mimi', last_name='Bolus', age=36)
#.objects.bulk_create()
mylist = [Patient(first_name='Adam', last_name='Smith', age=40), Patient(first_name='Karl', last_name='Marx', age=40)]
Patient.objects.bulk_create(mylist)


## Reading and Querying Database
#.all()
#if a str method is defined under the class it will return a QuerySet list that human readiable
Patient.objects.all()
"""
    .get() method grabs a single item from Model table 
    can be used with a single unique entry like the default
    primary key which is created by Django (pk=N)
"""
Patient.objects.get(pk=1)
"""
    .filter()
"""
Patient.objects.filter(last_name='Smith').all()
Patient.objects.filter(last_name='Smith').filter(age=40).all()
"""
    operators
"""
from django.db.models import Q
#AND
Patient.objects.filter(Q(last_name='Smith') & Q(age=40)).all()
#OR
Patient.objects.filter(Q(last_name='Smith') | Q(age=40)).all()

"""
    Filtering with Field Lookups
    for more complex filtering operations filed 
    lookups used with filter() call

    Model.objects.filter(name__startswith = 's')
"""
Patient.objects.filter(last_name__startswith = 's').all()
Patient.objects.filter(age__in=[20,30,40]).all()
Patient.objects.filter(age__gte=39).all()
Patient.objects.order_by('last_name').all()

"""
    Updating Models
    After updating models such as adding a field or a validator in a
    created field already you should migrate the changes by following code
    python manage.py makemigrations name_of_the_app_that_contains_the_changes_in_model
    python manage.py migrate
"""

"""
    Updating existing entries
    .save()
"""
carl = Patient.objects.get(pk=1)
carl.last_name = 'django'
carl.save()

"""
    Deleting entries
"""
data_point = Patient.objects.get(pk=2)
data_point.delete()

"""
    Connecting Data To Templates
    without forms and class based views (CBV)
"""