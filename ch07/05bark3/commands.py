import sys
import requests
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
    def execute(self, data, timestamp=None):
        data['data_added'] = timestamp or datetime.utcnow().isoformat()
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


class ImportGitHubStarsCommand:
    def _extract_bookmark_infor(self, repo):
        return {
            'タイトル': repo['name'],
            'URL': repo['html_url'],
            'メモ': repo['description'],
        }

    def execute(self, data):
        bookmarks_imported = 0

        github_username = data['github_username']
        next_page_of_results = \
            f'https://api.github.com/users/{github_username}/starred'

        while next_page_of_results:
            stars_response = requests.get(
                next_page_of_results,
                headers={'Accept': 'application/vnd.github.v3.star+json'},
            )
            next_page_of_results = stars_response.links.get(
                'next', {}).get('url')

            for repo_info in stars_response.json():
                repo = repo_info['repo']

                if data['preserve_timestamps']:
                    timestamp = datetime.strptime(
                        repo_info['starred_at'],
                        '%Y-%m-%dT%H:%M%SZ'
                    )
                else:
                    timestamp = None

                bookmarks_imported += 1
                AddBookmarkCommand().execute(
                    self._extract_bookmark_infor(repo),
                    timestamp=timestamp
                )
        return f'{bookmarks_imported}個のブックマークをインポートしました。'


class EditBookmarkCommand:
    def execute(self, data):
        db.update(
            'bookmarks',
            {'id': data['id']},
            data['update'],
        )
        return 'ブックマークを更新しました。'
