# duplicates in a list

some_list = ['a', 'b', 'c', 'd', 'a', 'b']
new_list = []
for i in some_list:
    count = some_list.count(i)
    # print(f'counting occurences for {i} element- {count}')
    if count > 1:
        if i not in new_list:
            new_list.append(i)


print(new_list)
