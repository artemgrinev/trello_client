import requests
import json
import sys

auth_params = {    
    'key': "bcda680e815b1edb071efbc7520a264c",    
    'token': "bdf01b18ec51d8b66d3c7d42e6dc6f6f88d5d4e73cb732a13a4c15e74f8f5a78", 
    }  
  
base_url = "https://api.trello.com/1/{}" 
board_id = "5ef0eb3a06c4957eae939363"
column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params=auth_params).json()

def read():
    """функция получет данные всех задач в колонке и перечисляет все названия"""
  
    for column in column_data:
        name = column['name']
        print(name)
        task_data = requests.get(base_url.format('lists') + '/' + column['id'] + '/cards', params=auth_params).json()
        
        len_task_data = len(task_data) % 10
        len_task_data_two = len(task_data) % 100
        if len_task_data == 1 and len_task_data_two != 11:
            print(f'{name}: одна задача')
        elif len_task_data in [2, 3, 4] and not (len_task_data_two in [12, 13, 14]):
            print(f'{name}: {len(task_data)} задачи')
        else:
            print(f'{name}: {len(task_data)} задач')

        if not task_data:
            print('\t' + 'Нет задач!')
            continue
        for task in task_data:
            print('\t' + task['name'])


def new_column(name):  
    return requests.post(base_url.format('lists'), data={'name': name, 'idBoard': board_id, **auth_params}).json()

def create(name, column_name):
    """функция позволяет создавать задачу с произвольным названием в одной из колонок"""
    for column in column_data:
        if column['name'] == column_name:  
            requests.post(base_url.format('cards'), data={'name': name, 'idList': column['id'], **auth_params})  
        break

def move(name, column_name):
    """Функция находит и перемещает задачу между колонками"""
    task_id = None
    for column in column_data:
        column_tasks = requests.get(base_url.format('lists') + '/' + column['id'] + '/cards', params=auth_params).json()    
        for task in column_tasks:
            if task['name'] == name:
                task_id = task['id']
                break
        if task_id:
            break

    for column in column_data:
        if column['name'] == column_name:
            requests.put(base_url.format('cards') + '/' + task_id + '/idList', data={'value': column['id'], **auth_params})
            break

if __name__ == "__main__":
    if len(sys.argv) <= 2:
        read()
    elif sys.argv[1] == 'create':
        create(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'move':
        move(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'new_column':
        new_column(sys.argv[2])