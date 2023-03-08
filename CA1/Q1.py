num_of_name, percent = input().split()
num_of_name = int(num_of_name)
percent = int(percent)
must_sort = int(num_of_name*percent/100)
name_list = input().split(',')
valus_list = input().split(',')


#sort valus_list and name_list
for i in range(num_of_name):
    for j in range(num_of_name-1):
        if int(valus_list[j]) < int(valus_list[j+1]):
            valus_list[j], valus_list[j+1] = valus_list[j+1], valus_list[j]
            name_list[j], name_list[j+1] = name_list[j+1], name_list[j]



final_name_list = name_list[0:must_sort]
del name_list[0:must_sort]
#sort name_list with letters

#print final_name_list
for i in range(must_sort):
     print(final_name_list[i], end = ' ')
for ele in sorted(name_list):
    print(ele, end = ' ')