from logging import exception

from config.wsgi import *
from core.erp.models import Type, Employee

# SELECT
# Select * from Tabla
#query = Type.objects.all()
#print(query)

# INSERT
# t = Type()
# t.name = 'test'
# t.save()
#-----
#t = Type(name='Terry Gilliam').save()


# UPDATE
# try:
#     t = Type.objects.get(id=1) #id or pk.. siempre tiene que existir y no estar repetido para usar get
#     t.name = 'test51'
#     t.save()
# except Exception as e:
#     print(e)

# DELETE
# t = Type.objects.get(id=1)
# t.delete()

# Metodo FILTER
#t = Type.objects.filter(name__contains='pre')
#t = Type.objects.filter(name__icontains='terry')
#t = Type.objects.filter(name__in=['viba','hola'])
#for i in Type.objects.filter(name__endswith='a')[0:2]:
#    print(i.name)
#Excluir los empleados del tipo 1
#t = Employee.objects.filter(type_id=1).exclude(state=False)






