my_dict={'pavel':1991, 'alla':1992, 'roman':1988, 'olga':1991}
print(my_dict)
print(my_dict.get('pavel'))
print(my_dict.get('pasha'))
my_dict['anton']=1993
my_dict.update({'masha':1997, 'misha':2000})
a=my_dict.pop('roman')
print(a)
print(my_dict)


my_set={11,12,12.5,11,'value',12.5,12.8,'string','value','банан','банан'}
print(my_set)
my_set.add(6)
my_set.add((6,7,8))
my_set.add('рыбка')
my_set.discard(12.5)
print(my_set)