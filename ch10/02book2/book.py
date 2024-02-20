class Book:
    def __init__(self, title, subtitle, author):
        self.title = title
        self.subtitle = subtitle
        self.author = author

    def display_info(self):
        print(f'{self.author}著『{self.title} ── {self.subtitle}』')


book = Book(author='デイン・ディラード', title='Pythonプロフェッショナル・プログラミング',
            subtitle='一流のPythonプログラマーへのパスポート')
book.display_info()
