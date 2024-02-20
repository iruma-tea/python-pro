class Book:
    def __init__(self, title, subtitle, author):
        self.title = title
        self.subtitle = subtitle
        self.author = author


def display_book_info(book):
    print(f'{book.author}著『{book.title} ── {book.subtitle}』')


book = Book(author='デイン・ディラード', title='Pythonプロフェッショナル・プログラミング', subtitle='一流のPythonプログラマーへのパスポート')
display_book_info(book)
