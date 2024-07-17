immutable_var = (1,2,'one','two')
print(immutable_var)
#immutable_var [1]='two'
#Traceback (most recent call last):
#  File "C:\Homework\Homework5.py", line 3, in <module>
#    immutable_var [1]='two'
#    ~~~~~~~~~~~~~~^^^
#TypeError: 'tuple' object does not support item assignment
#В кортеже сами обьекты не меняются. Кортеж создавалами как список , который не может измениться.
#Еще одной особенностью является меньшее занимаемое место в памяти.
#Сам кортеж мы не можем изменить, лишь только часть его содержимого

mutable_list = [1, 2 ,'ten', 'eleven']
mutable_list.append('twelve')
print(mutable_list)
mutable_list[0]=12
print(mutable_list)