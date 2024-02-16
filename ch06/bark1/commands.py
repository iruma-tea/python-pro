import sys
from datetime import datetime
from database import DatabaseManager

db = DatabaseManager('bookmarks.db')


class CreateBookmarksTableCommand:
    def execute(self):
        db.create_table('bookmarks', {
            'id': 'integer primary key autoincrement',
            'title': 'text not null',
            'url': 'text not null',
            'notes': 'text',
            'data_added': 'text not null',
        })


class AddBookmarkCommand:
    def execute(self, data):
        data['data_added'] = datetime.utcnow().isoformat()
        db.add('bookmarks', data)
        return 'ブックマークを追加しました。'


class ListBookmarksCommand:
    def __init__(self, order_by='data_added'):
        self.order_by = order_by

    def execute(self):
        return db.select('bookmarks', order_by=self.order_by).fetchall()  # <2>


class DeleteBookmarkCommand:
    def execute(self, data):
        db.delete('bookmarks', {'id': data})  # <1>
        return 'ブックマークを削除しました。'


class QuitCommand:
    def execute(self):
        sys.exit()
