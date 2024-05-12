import datetime
import json

class Note:
    def __init__(self, name, content, existing=False):
        if not existing:
            self.name = name
            self.content = content
            self.creation_date = datetime.datetime.strftime(datetime.datetime.now(), r'%Y/%m/%d %H:%M')
            self.upd_last_modified_date()
        else:
            _dict = json.load(open(f'./notes/{name}.json','r',encoding='utf-8'))
            self.name = _dict['name']
            self.content = _dict['content']
            self.creation_date = _dict['creation_date']
            self.last_modifed_date = _dict['last_modified_date']
    def upd_last_modified_date(self): self.last_modifed_date = datetime.datetime.strftime(datetime.datetime.now(), r'%Y/%m/%d %H:%M')
    def edit_name(self, name):
        self.name=name
        self.upd_last_modified_date()
    def edit_content(self, content):
        self.content = content
        self.upd_last_modified_date()
    def return_dict(self):
        return {
            "name": self.name,
            "content": self.content,
            "creation_date": self.creation_date,
            "last_modified_date": self.last_modifed_date,
        }