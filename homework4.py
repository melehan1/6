immutable_var = (1, 2.2, 'korteg')
print(immutable_var)
#immutable_var[1] = 200 #кортеж не поддерживает обращение по элементам, он неизменяемый!
#immutable_var.append('200')
mutable_list = [1, 2.2, 'spisok']
mutable_list[2] = 200
mutable_list.append('Modified')
print(mutable_list)
