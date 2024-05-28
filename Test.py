# with open('random.txt', 'w') as file:
#     user_input = input('Введите текст ')
#     file.write(user_input)


# with open('28.05.2024.txt','w') as file:
#     file.write('Hello world')    


my_list = ['apple', 'banana', 'orange', 'grape']
with open('list_random.txt','w') as file:
    for i in my_list:
        file.write(f'{i}\n')