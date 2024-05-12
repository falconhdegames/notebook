import note
import os
import json

def check():
    if not os.path.exists('./notes'): os.makedirs('./notes')

def export(nt):
    check()
    json.dump(nt.return_dict(), open(f'./notes/{nt.name}.json', 'w', encoding='utf-8'))

def remove(name):
    os.remove(f'./notes/{name}.json')