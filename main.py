import note
import export
import sys
import os

def no_err_input(msg):
    while True:
        _input = input(msg)
        if _input == '\n' or _input == '':
            print('Не оставляйте пустое значение!')
            continue
        else: return _input

def add(name=None, content=None):
    if not name: name = no_err_input('Введите заголовок заметки: ')
    if not content: content = no_err_input('Введите тело заметки: ')
    export.export(note.Note(name, content))
    print('Заметка успешно сохранена!')

def edit(orig_name=None, name=None, content=None):
    if not orig_name: orig_name = no_err_input('Введите заголовок оригинальной заметки: ')
    if not name: name = no_err_input('Введите изменённый заголовок заметки: ')
    if not content: content = no_err_input('Введите изменённое тело заметки: ')
    try:
        nt = note.Note(orig_name, None, True)
        nt.edit_name(name)
        nt.edit_content(content)
        export.remove(orig_name)
        export.export(nt)
        print('Заметка успешно изменена!')
    except:
        print('Заметка с таким именем не существует!')

def delete(name=None):
    if not name: name = no_err_input('Введите заголовок заметки: ')
    try:
        export.remove(name)
        print('Заметка успешно удалена!')
    except:
        print('Заметка с таким именем не существует!')

def read(name=None):
    if not name: name = no_err_input('Введите заголовок заметки: ')
    print(note.Note(name, None, True).content)

def list_notes():
    lst = []
    for file in os.listdir('./notes'): lst.append('.'.join(file.split('.')[:-1]))
    print(*lst, sep='\n')

def read_args():
    args = {}
    for index, arg in enumerate(sys.argv):
        if arg.startswith('--'):
            try:
                args[arg[2:]] = sys.argv[index+1]
            except:
                print('Синтаксическая ошибка! После флагов должно быть значение!')
                sys.exit(1)
    return args

if __name__ == "__main__":
    if len(sys.argv) != 1:
        args = read_args()
        if sys.argv[1] == 'add':
            try: add(args['name'], args['content'])
            except: print('Неверные аргументы!')
        elif sys.argv[1] == 'edit':
            try: edit(args['orig_name'], args['name'], args['content'])
            except: print('Неверные аргументы!')
        elif sys.argv[1] == 'delete':
            try: delete(args['name'])
            except: print('Неверные аргументы!')
        elif sys.argv[1] == 'list':
            list_notes()
        elif sys.argv[1] == 'read':
            try: read(args['name'])
            except: print('Неверные аргументы!')
    else:
        while True:
            cmd = no_err_input('Введите команду: ')
            if cmd == 'add': add()
            elif cmd == 'edit': edit()
            elif cmd == 'delete': delete()
            elif cmd == 'list': list_notes()
            elif cmd == 'read': read()
            elif cmd == 'exit': sys.exit('0')
            else: print('Неизвестная команда!')