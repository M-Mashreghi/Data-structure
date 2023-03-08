num_of_name, percent = input().split()
num_of_name,percent = int(num_of_name),int(percent)
must_sort =int(num_of_name*percent/100)
name_list = input().split(',')
valus_list = input().split(',')
data = []
for i in range(num_of_name):
    data.append((int(valus_list[i]),name_list[i]))

def take_value(elem):
    return elem[0]
data= sorted(data, key=take_value,reverse=True)


def take_name(elem):
    return elem[1]

for i in range(must_sort):
     print(data[i][1], end = ' ')

     
del data[0:must_sort]


data= sorted(data, key=take_name)
for i in range(len(data)):
     print(data[i][1], end = ' ')
