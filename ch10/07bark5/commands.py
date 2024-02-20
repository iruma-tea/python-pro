import sys
from abc import ABC, abstractclassmethod
from datetime import datetime

import requests

from database import DatabaseManager

db = DatabaseManager('bookmarks.db')


class Command(ABC):
    @abstractclassmethod
    def execute(self, data):
        raise NotImplementedError('コマンドは必ずメソッドexecuteを実装してください')


class CreateBookmarksTableCommand(Command):
    def execute(selfm, data=None):
        db.create_table('bookmarks', {
            'id': 'integer primary key autoincrement',
            'タイトル': 'text not null',
            'URL': 'text not null',
            'メモ': 'text',
            '追加日時': 'text not null',
        })


class AddBookmarkCommand(Command):
    def execute(self, data, timestamp=None):
        data['追加日時'] = timestamp or datetime.utcnow().isoformat()
        db.add('bookmarks', data)
        return 'ブックマークを追加しました。'


class ListBookmarksCommand(Command):
    def __init__(self, order_by='追加日時'):
        self.order_by = order_by

    def execute(self, data=None):
        return db.select('bookmarks', order_by=self.order_by).fetchall()


class DeleteBookmarkCommand(Command):
    def execute(self, data):
        db.delete('bookmarks', {"id": data})
        return 'ブックマークを削除しました。'


class QuitCommand(Command):
    def execute(self, data=None):
        sys.exit()


class ImportGitHubStarsCommand(Command):
    def _extract_bookmark_info(self, repo):
        return {
            'タイトル': repo['name'],
            'URL': repo['html_url'],
            'メモ': repo['description'],
        }

    def execute(self, data):
        bookmarks_imported = 0
        github_username = data['github_username']
        next_page_of_results = f'https://api.github.com/users/{
            github_username}/starred'

        while next_page_of_results:
            starts_response = requests.get(
                next_page_of_results,
                headers={'Accept': 'application/vnd.github.v3.star+json'},
            )
            next_page_of_results = starts_response.links.get(
                'next', {}).get('url')

            for repo_info in starts_response.json():
                repo = repo_info['repo']

                if data['preserve_timestamps']:
                    timestamp = datetime.strptime(
                        repo_info['starred_at'],
                        '%Y-%m-%dT%H:%M:%SZ'
                    )
                else:
                    timestamp = None

                bookmarks_imported += 1
                AddBookmarkCommand().execute(
                    self._extract_bookmark_info(repo),
                    timestamp=timestamp
                )
        return f'{bookmarks_imported}個のブックマークをインポートしました。'


class EditBookmarkCommand(Command):
    def execute(self, data):
        db.update(
            'bookmarks',
            {'id': data['id']},
            data['update'],
        )
        return 'ブックマークを更新しました。'
